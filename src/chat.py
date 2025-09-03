import os
from search import search_prompt
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

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
        question = input("Digite sua pergunta (ou 'sair' para encerrar): ")

        if not question.strip():
            print("Por favor, insira uma pergunta válida.")
            continue

        if question.lower() == "sair":
            break

        chain = search_prompt()

        if not chain:
            print(
                "Não foi possível iniciar o chat. Verifique os erros de inicialização."
            )
            return

        context = get_context(question)

        response = chain.invoke(
            {"pergunta": question, "contexto": context}, config=config
        )

        print("Resposta:", response.content.strip())
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
