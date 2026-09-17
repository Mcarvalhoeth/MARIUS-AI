from core.llm import ask

def main():
    print("Marius AI online. Digite 'sair' para encerrar.")
    while True:
        message = input("Você: ").strip()
        if message.lower() in {"sair", "exit", "quit"}:
            print("Marius AI encerrado.")
            break
        if message:
            try:
                print("Marius:", ask(message))
            except Exception as error:
                print("Erro:", error)

if __name__ == "__main__":
    main()
