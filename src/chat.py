import os
from search import search_prompt
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from utils import print_colored, input_colored

config = {"configurable": {"session_id": "chat-session"}}


def get_context(question: str) -> str:
    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_MODEL", "text-embedding-3-small")
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PGVECTOR_COLLECTION"),
        connection=os.getenv("PGVECTOR_URL"),
        use_jsonb=True,
    )

    results = store.similarity_search_with_score(question, k=10)
    contents = [doc.page_content.strip() for doc, _ in results]

    return "\n\n".join(contents)


def main():
    while True:
        print("\n\n")
        print_colored("Busca Semântica com LangChain e Postgres.", "blue")
        print_colored(
            "\nPergunte algo sobre as empresas contidas no banco de dados.\n",
            "green",
        )
        print_colored("Exemplo de pergunta que você pode fazer:", "green")
        print_colored("- Qual o faturamento da Empresa SuperTechIABrazil?", "green")
        print_colored(
            "\n\nIniciando chat. Digite 'sair' para encerrar.\n",
            "green",
        )

        question = input_colored(
            "Digite sua pergunta (ou 'sair' para encerrar): ", "blue"
        )

        if not question.strip():
            print_colored("Por favor, insira uma pergunta válida.", "red")
            continue

        if question.lower() == "sair":
            break

        chain = search_prompt()

        if not chain:
            print_colored(
                "Não foi possível iniciar o chat. Verifique os erros de inicialização.",
                "red",
            )
            return

        context = get_context(question)

        response = chain.invoke(
            {"pergunta": question, "contexto": context}, config=config
        )

        print_colored("Resposta:", response.content.strip(), "green")
        print_colored("\n" + "-" * 50 + "\n", "yellow")


if __name__ == "__main__":
    main()
