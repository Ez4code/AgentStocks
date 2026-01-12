import os
qwen_api_key = os.getenv("DASHSCOPE_API_KEY")

CONFIG = {
    "chatgpt": {
        "api_key": "OPENAI_API_KEY",
        "model_name": "gpt-4o-mini",
    },
    "qwen": {
        "api_key": qwen_api_key,
        "model_name": "qwen-max",
        #"model_name": "qwen3-max-thinking-preview",
    },
    "deepseek": {
        "api_key": "DEEPSEEK_API_KEY",
        "model_name": "deepseek-chat",
    },
}
# For verification purpose
print("qwen_api_key:", CONFIG["qwen"]["api_key"])
