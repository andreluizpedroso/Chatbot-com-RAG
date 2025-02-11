# 🚀 Projeto: Chatbot com RAG usando LangChain e FAISS  

Este projeto implementa um **chatbot inteligente** que utiliza **IA Generativa com RAG (Retrieval-Augmented Generation)** para responder perguntas baseadas no conteúdo de um **PDF**. Ele usa **LangChain**, **FAISS** e **OpenAI GPT-4** para criar um sistema de busca e geração de respostas precisas.

---

## 🌜 **Descrição do Projeto**  
O chatbot permite que os usuários façam perguntas sobre o conteúdo de um livro em PDF e obtenham respostas geradas pela IA com base no próprio documento. Isso é possível por meio da técnica **RAG**, onde a IA primeiro recupera informações relevantes do texto antes de gerar uma resposta.

**Principais Tecnologias:**  
✅ **LangChain** - Framework para integração de IA com bases de conhecimento  
✅ **FAISS** - Banco de dados vetorial para busca semântica  
✅ **OpenAI GPT-4** - Modelo de IA para geração de respostas  
✅ **PyMuPDF** - Extração de texto de PDFs  
✅ **tiktoken** - Contagem de tokens para otimização  

---

## 💂 **Requisitos**
Antes de rodar o projeto, certifique-se de que possui os seguintes requisitos:
- Python 3.8+
- Chave de API da OpenAI

---

## 📚 **Estrutura do Projeto**  

```
📦 chatbot-rag
 ┣ 📚 data/                # Pasta onde ficam os PDFs processados
 ┣ 📚 models/              # Banco vetorial FAISS salvo
 ┣ 📚 src/                 # Código-fonte principal do projeto
 ┃ ┣ 📜 main.py           # Código principal do chatbot
 ┃ ┣ 📜 process_pdf.py    # Módulo para processar PDFs e gerar embeddings
 ┃ ┣ 📜 query_bot.py      # Módulo para consultas ao chatbot
 ┣ 📜 requirements.txt    # Dependências do projeto
 ┣ 📜 README.md           # Documentação do projeto
```

---

## 🚀 **Instalação e Configuração**

### 1️⃣ **Clone este repositório**  
```bash
git clone https://github.com/seu-usuario/chatbot-rag.git
cd chatbot-rag
```

### 2️⃣ **Instale as dependências**  
```bash
pip install -r requirements.txt
```

### 3️⃣ **Defina sua API Key da OpenAI**  
No terminal:
```bash
export OPENAI_API_KEY="sua_api_key_aqui"
```
Ou crie um arquivo `.env` e adicione:
```env
OPENAI_API_KEY=sua_api_key_aqui
```

### 4️⃣ **Execute o chatbot**  
```bash
python src/main.py
```

---

## 🔎 **Como Funciona?**
1️⃣ O PDF é carregado e processado em **blocos de texto**.  
2️⃣ Cada bloco é convertido em **embeddings vetoriais** e salvo no **FAISS**.  
3️⃣ Quando o usuário faz uma pergunta, o chatbot **busca no banco vetorial** as partes mais relevantes do documento.  
4️⃣ O **GPT-4** usa essas informações para gerar uma resposta precisa.  
