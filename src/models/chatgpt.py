from openai import OpenAI
from base import BaseLLM


class ChatGPT(BaseLLM):
    def __init__(self, api_key: str, model_name="gpt-4o-mini"):
        super().__init__(model_name)
        self.client = OpenAI(api_key=api_key)

    def chat(self, prompt: str, **kwargs) -> str:
        resp = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=kwargs.get("temperature", 0.2),
        )
        return resp.choices[0].message.content
