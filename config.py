import os
from langchain_openai import ChatOpenAI

def get_llm(model="qwen-max"):
    """
    返回一个可用的 Qwen-Max LLM 实例
    """
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("QWEN_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # Qwen OpenAI 兼容接口
        temperature=0.3,
        max_tokens=8000
    )
