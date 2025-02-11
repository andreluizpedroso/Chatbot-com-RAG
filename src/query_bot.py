import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# Definir chave da OpenAI
os.environ["OPENAI_API_KEY"] = "sua_api_key_aqui"

def load_chatbot(vector_store_path="models/banco_vetorial"):
    """Carrega o banco vetorial FAISS e cria o chatbot RAG."""
    
    print("🔄 Carregando banco vetorial...")
    vector_store = FAISS.load_local(vector_store_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

    print("🤖 Configurando modelo de IA...")
    llm = ChatOpenAI(model_name="gpt-4")

    print("🔗 Criando pipeline de perguntas e respostas...")
    qa_chain = load_qa_chain(llm, chain_type="stuff")
    qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=vector_store.as_retriever())

    return qa

def query_bot(pergunta, chatbot):
    """Faz uma pergunta ao chatbot e retorna a resposta."""
    resposta = chatbot.run(pergunta)
    return resposta

if __name__ == "__main__":
    chatbot = load_chatbot()
    while True:
        pergunta = input("\n❓ Pergunta (ou 'sair' para encerrar): ")
        if pergunta.lower() == "sair":
            break
        resposta = query_bot(pergunta, chatbot)
        print("\n📖 Resposta:", resposta)
