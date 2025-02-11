import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# Definir chave da OpenAI
os.environ["OPENAI_API_KEY"] = "sua_api_key_aqui"

def process_pdf(pdf_path, vector_store_path="models/banco_vetorial"):
    """Processa um PDF e gera embeddings para FAISS."""
    
    print("🔍 Carregando documento...")
    loader = PyMuPDFLoader(pdf_path)
    docs = loader.load()

    print("📖 Dividindo texto em segmentos...")
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(docs)

    print("🔢 Criando embeddings...")
    embeddings = OpenAIEmbeddings()

    print("💾 Criando banco vetorial FAISS...")
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(vector_store_path)

    print("✅ Banco vetorial salvo em:", vector_store_path)

if __name__ == "__main__":
    pdf_file = "data/andrew-ng-machine-learning-yearning.pdf"
    process_pdf(pdf_file)
