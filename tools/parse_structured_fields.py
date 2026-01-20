import re

def parse_structured_fields(text: str):
    up_prob = None
    down_prob = None

    clean_text = text.replace("**", "").replace("*", "")

    up_match = re.search(r"UP_PROB\s*:\s*([0-9.]+)", clean_text)
    down_match = re.search(r"DOWN_PROB\s*:\s*([0-9.]+)", clean_text)

    if up_match:
        up_prob = float(up_match.group(1))

    if down_match:
        down_prob = float(down_match.group(1))

    return up_prob, down_prob
