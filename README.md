## 🧠 RAG Chatbot com PDFs – Customizável para Qualquer Setor

Este projeto é um **chatbot inteligente com RAG (Retrieval-Augmented Generation)** desenvolvido para responder perguntas com base em documentos PDF de até **200 MB**. Ideal para escritórios de advocacia, mas **totalmente customizável** para outros setores.

Construído com **LangChain**, **OpenAI GPT-4o-mini**, e interface amigável em **Streamlit**.

* Acesse em: https://lawchatbotpdf.streamlit.app/

---

## 🚀 Funcionalidades

* 💬 Chat com PDFs usando **RAG (Retrieval-Augmented Generation)**
* 🧩 Quebra de documentos em **chunks semânticos** com embeddings vetoriais
* 📚 Suporte para **arquivos PDF grandes (até 200 MB)**
* ⚙️ API da **OpenAI** com **modelo GPT-4o-mini** para geração de respostas
* 🔎 Busca inteligente de contexto nos documentos via **vector store**
* 🖥️ Interface leve e interativa com **Streamlit**
* 🔁 **Prompt customizável** para qualquer domínio de conhecimento

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

| Componente                           | Tecnologia                              |
| ------------------------------------ | --------------------------------------- |
| RAG (Retrieval-Augmented Generation) | `LangChain`                             |
| LLM                                  | `GPT-4o-mini` via OpenAI API            |
| Vetorização (Embeddings)             | `OpenAIEmbeddings`                      |
| Armazenamento Vetorial               | `FAISS`, `Chroma` ou outro configurável |
| Leitura de PDFs                      | `PyMuPDF` (`fitz`) ou `pdfminer`        |
| Interface                            | `Streamlit`                             |
| Backend                              | `Python 3.12+`                          |

---

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/chatbot-rag-pdf.git
cd chatbot-rag-pdf
pip install -r requirements.txt
```

---

## 🔐 Configuração de Variáveis (Streamlit Secrets)

> ⚠️ Para que o projeto funcione corretamente, é necessário configurar suas **chaves de API no `streamlit.secrets`**.

Crie um arquivo chamado `.streamlit/secrets.toml` com o seguinte conteúdo:

```toml
[openai]
api_key = "sk-sua-chave-aqui"
```

Alternativamente, no deploy online (ex: Streamlit Cloud), adicione essa variável diretamente em **Settings > Secrets**.

---

## ▶️ Executando o Projeto

```bash
streamlit run app.py
```

---

## 🔧 Customização

Você pode facilmente adaptar este projeto para outros setores:

* Alterando o **prompt principal** no código LangChain.
* Usando documentos de qualquer área (direito, saúde, contabilidade...).
* Trocando o sistema de embeddings ou o vector store.
* Implementando filtros por documentos, autores ou palavras-chave.

---

## 💡 Exemplos de Aplicação

* 👩‍⚖️ Escritório de advocacia: perguntas sobre contratos, petições, decisões.
* 🌽 Agronegócio: análise de laudos técnicos, relatórios de produção.
* 🧾 Contabilidade: interpretação de balancetes, notas fiscais.
* 🏥 Saúde: análise de laudos, protocolos clínicos.
* 🧪 Pesquisa científica: revisão de artigos e papers técnicos.

---

## 📄 Licença

MIT License

---