from models.chatgpt import ChatGPT
from models.qwen import Qwen
from models.deepseek import DeepSeek


class AIAnalyst:
    """
    Unified AI Analyst for multi-LLM access.
    """

    def __init__(self, cfg: dict):
        self.models = {}

        if "chatgpt" in cfg:
            self.models["chatgpt"] = ChatGPT(**cfg["chatgpt"])

        if "qwen" in cfg:
            self.models["qwen"] = Qwen(**cfg["qwen"])

        if "deepseek" in cfg:
            self.models["deepseek"] = DeepSeek(**cfg["deepseek"])

    def chat(self, model: str, prompt: str, **kwargs) -> str:
        if model not in self.models:
            raise ValueError(f"Model {model} not initialized")

        return self.models[model].chat(prompt, **kwargs)

    def compare(self, prompt: str) -> dict:
        """
        Send same prompt to all models.
        """
        results = {}
        for name, m in self.models.items():
            results[name] = m.chat(prompt)
        return results

def Load_System_Prompt(file_path: str) -> str:
    """从文件中读取系统提示词"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()