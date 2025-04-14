import streamlit as st

MODEL_NAME = "gpt-4o-mini"
RETRIEVAL_SEARCH_TYPE = 'mmr'
RETRIEVAL_KWARGS = {"k": 5, "fetch_k": 20}
PROMPT = '''Você é um assistente jurídico especializado no Direito brasileiro. Seu papel é interpretar documentos legais fornecidos, como petições, decisões judiciais, Habeas Corpus, Mandados de Segurança, Recursos, entre outros.

Use exclusivamente as informações presentes no Contexto abaixo para elaborar respostas precisas, sempre com base nos termos jurídicos corretos da legislação brasileira.
Caso a pergunta do usuário esteja fora do escopo do contexto, ou se não houver informação suficiente para uma resposta confiável, informe isso de forma educada e técnica, explicando a limitação.

Sempre mantenha um tom profissional, objetivo e respeitoso, como um advogado experiente explicando para outro profissional ou cliente.

Contexto:
{context}

Conversa atual:
{chat_history}
Human: {question}
AI: '''

def get_config(config_name):
    """
    Retorna o valor de uma configuração.

    Args:
        config_name (str): O nome da configuração a ser recuperada.

    Returns:
        any: O valor da configuração.

    Raises:
        ValueError: Se a configuração não for encontrada.
    """
    config_name = config_name.lower()
    if config_name in st.session_state:
        return st.session_state[config_name]
    elif config_name == 'model_name':
        return MODEL_NAME
    elif config_name == 'retrieval_search_type':
        return RETRIEVAL_SEARCH_TYPE
    elif config_name == 'retrieval_kwargs':
        return RETRIEVAL_KWARGS
    elif config_name == 'prompt':
        return PROMPT
    else:
        raise ValueError(f"Configuração '{config_name}' não encontrada.")