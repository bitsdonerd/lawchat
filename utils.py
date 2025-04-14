from pathlib import Path
import os
import streamlit as st

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from configs import get_config  # Certifique-se que configs.py retorna configs corretos

# Caminho da pasta onde os PDFs são armazenados
PASTA_ARQUIVOS = Path(__file__).parent / 'arquivos'


def importacao_documentos():
    documentos = []
    for arquivo in PASTA_ARQUIVOS.glob('*.pdf'):
        loader = PyPDFLoader(str(arquivo))
        documentos_arquivo = loader.load()
        documentos.extend(documentos_arquivo)
    return documentos


def split_de_documentos(documentos):
    recur_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2500,
        chunk_overlap=250,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    documentos = recur_splitter.split_documents(documentos)

    for i, doc in enumerate(documentos):
        doc.metadata['source'] = Path(doc.metadata['source']).name
        doc.metadata['doc_id'] = i
    return documentos


def cria_vector_store(documentos):
    # Define a variável de ambiente exigida pela nova versão
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

    # Criação do embedding model usando a API nova
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-large"  # Use o modelo mais atual
    )

    vector_store = FAISS.from_documents(
        documents=documentos,
        embedding=embedding_model
    )
    return vector_store


def cria_chain_conversa():
    # Verifica se a chave da API foi definida
    OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY não encontrada.")

    # Garante que a variável de ambiente esteja setada
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    # Etapas da pipeline
    documentos = importacao_documentos()
    documentos = split_de_documentos(documentos)
    vector_store = cria_vector_store(documentos)

    # Instancia o modelo de chat
    chat = ChatOpenAI(
        model=get_config('model_name'),  # Ex: "gpt-4", "gpt-3.5-turbo"
        temperature=0.3
    )

    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key='chat_history',
        output_key='answer'
    )

    retriever = vector_store.as_retriever(
        search_type=get_config('retrieval_search_type'),
        search_kwargs=get_config('retrieval_kwargs')
    )

    prompt = PromptTemplate.from_template(get_config('prompt'))

    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=chat,
        memory=memory,
        retriever=retriever,
        return_source_documents=True,
        verbose=True,
        combine_docs_chain_kwargs={'prompt': prompt}
    )

    st.session_state['chain'] = chat_chain

