import requests
from base import BaseLLM


class DeepSeek(BaseLLM):
    def __init__(self, api_key: str, model_name="deepseek-chat"):
        super().__init__(model_name)
        self.api_key = api_key
        self.url = "https://api.deepseek.com/v1/chat/completions"

    def chat(self, prompt: str, **kwargs) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": kwargs.get("temperature", 0.2),
        }

        # r = requests.post(self.url, json=payload, headers=headers, timeout=30)
        # r.raise_for_status()
        # return r.json()["choices"][0]["message"]["content"]
