import os
from pathlib import Path
from openai import OpenAI

def load_key():
    env_file = Path.home() / ".hermes" / ".env"
    for line in env_file.read_text().splitlines():
        if line.startswith("OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip()
    return os.getenv("OPENAI_API_KEY")

def ask(message: str) -> str:
    client = OpenAI(api_key=load_key())
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=message,
    )
    return response.output_text
