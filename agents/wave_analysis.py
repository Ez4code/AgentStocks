from langchain_openai import ChatOpenAI
from prompts.loader import load_prompt
from config import get_llm
from tools.parse_structured_fields import parse_structured_fields

llm = get_llm(model="qwen-max")

def market_context_node(state):
    prompt = load_prompt("market_context.txt")

    resp = llm.invoke(prompt.format(
        stock_name=state["stock_name"]
    ))

    # test point
    print("=== market_context_node 原始返回 ===")
    print(resp.content)
    #

    return {
        "market_context": resp.content
    }

def wave_analysis_node(state):
    prompt = load_prompt("wave_analysis.txt")

    resp = llm.invoke(prompt.format(
        stock_name=state["stock_name"],
        market_context=state["market_context"]
    ))

    content = resp.content
    
    # test point
    print("=== wave_analysis_node 原始返回 ===")
    print(content)
    #
    up_prob, down_prob = parse_structured_fields(content)
    
    if up_prob is None or down_prob is None:
        print("⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️")
        print("⚠️⚠️⚠️ 概率未按格式返回，使用默认值 0.5⚠️⚠️⚠️")
        print("⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️")
        up_prob = 0.5
        down_prob = 0.5

    return {
        "wave_analysis": content,
        "up_prob": up_prob,
        "down_prob": down_prob
    }
