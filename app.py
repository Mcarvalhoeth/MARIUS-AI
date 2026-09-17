"""Ponto de entrada inicial do Marius AI."""

from core.orchestrator import route

def main():
    print("Marius AI online. Digite 'sair' para encerrar.")
    while True:
        message = input("Você: ").strip()
        if message.lower() in {"sair", "exit", "quit"}:
            print("Marius AI encerrado.")
            break
        if message:
            print(f"Módulo selecionado: {route(message)}")

if __name__ == "__main__":
    main()
