from search import search_prompt

config = {"configurable": {"session_id": "chat-session"}}


def main():
    while True:
        question = input("Digite sua pergunta (ou 'sair' para encerrar): ")

        if not question.strip():
            print("Por favor, insira uma pergunta válida.")
            continue

        if question.lower() == "sair":
            break

        chain = search_prompt(question)

        if not chain:
            print(
                "Não foi possível iniciar o chat. Verifique os erros de inicialização."
            )
            return

        response = chain.invoke({"pergunta": question}, config=config)

        print("Resposta:", response.content.strip())
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
