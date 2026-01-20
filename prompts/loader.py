from pathlib import Path

PROMPT_DIR = Path(__file__).parent

def load_prompt(name):
    path = PROMPT_DIR / name
    return path.read_text(encoding="utf-8")
