from core.llm import ask
from core.orchestrator import route
from agents.agenda import prompt as agenda_prompt
from agents.mercado import prompt as mercado_prompt
from agents.cripto import prompt as cripto_prompt

def main():
    print("Marius AI online. Digite 'sair' para encerrar.")

    while True:
        message = input("Você: ").strip()

        if message.lower() in {"sair", "exit", "quit"}:
            break

        if not message:
            continue

        area = route(message)

        if area == "agenda":
            message = agenda_prompt(message)
        elif area == "mercado":
            message = mercado_prompt(message)
        elif area == "cripto":
            message = cripto_prompt(message)

        print("Marius:", ask(message))

if __name__ == "__main__":
    main()
