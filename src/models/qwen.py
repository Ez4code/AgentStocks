import dashscope
from base import BaseLLM


class Qwen(BaseLLM):
    def __init__(self, api_key: str, model_name="qwen-turbo"):
        super().__init__(model_name)
        dashscope.api_key = api_key

    def chat(self, prompt: str, **kwargs) -> str:
        resp = dashscope.Generation.call(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=kwargs.get("temperature", 0.2),
        )
        return resp.output.text
