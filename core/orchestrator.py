"""Núcleo inicial do Marius AI."""

def classify(message: str) -> str:
    text = message.lower()

    areas = {
        "agenda": ("agenda", "reunião", "compromisso", "lembrete"),
        "email": ("e-mail", "email"),
        "mercado": ("selic", "juros", "bolsa", "dólar", "mercado"),
        "cripto": ("bitcoin", "btc", "ethereum", "cripto", "token"),
        "radar": ("notícia", "noticias", "novidade"),
    }

    for area, terms in areas.items():
        if any(term in text for term in terms):
            return area

    return "assistente"

def route(message: str) -> str:
    return classify(message)
