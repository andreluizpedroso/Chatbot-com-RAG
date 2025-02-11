import os
from src.process_pdf import process_pdf
from src.query_bot import load_chatbot, query_bot

# Caminho do PDF e banco vetorial
PDF_PATH = "data/andrew-ng-machine-learning-yearning.pdf"
VECTOR_STORE_PATH = "models/banco_vetorial"

def main():
    """Executa o chatbot carregando ou criando o banco vetorial."""
    
    if not os.path.exists(VECTOR_STORE_PATH):
        print("⚙️ Processando PDF para gerar banco vetorial...")
        process_pdf(PDF_PATH, VECTOR_STORE_PATH)

    chatbot = load_chatbot(VECTOR_STORE_PATH)
    
    print("\n🤖 Chatbot pronto! Faça suas perguntas.")
    while True:
        pergunta = input("\n❓ Pergunta (ou 'sair' para encerrar): ")
        if pergunta.lower() == "sair":
            print("👋 Encerrando chatbot. Até mais!")
            break
        resposta = query_bot(pergunta, chatbot)
        print("\n📖 Resposta:", resposta)

if __name__ == "__main__":
    main()
