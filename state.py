from typing import TypedDict

class AgentState(TypedDict):
    stock_name: str


    # LLM 生成的市场认知数据
    market_context: str

    # 波浪分析输出
    wave_analysis: str

    up_prob: float
    down_prob: float



# 主趋势方向：
# 当前波浪阶段：
# 关键支撑位：
# 关键压力位：
# 最高概率波浪路径：
# 次高概率波浪路径：
# 分析失效触发条件：
