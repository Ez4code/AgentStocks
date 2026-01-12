from core import AIAnalyst
from core import Load_System_Prompt 
from config import CONFIG


ai = AIAnalyst(CONFIG)

# prompt = "用一句话解释什么是流水线CPU"

prompt = Load_System_Prompt("/Users/liuxin/Project/AgentStocks/src/system_prompt.txt")

# 单模型
print(ai.chat("qwen", prompt))

# 多模型对比
# results = ai.compare(prompt)
# for k, v in results.items():
#     print(f"\n[{k.upper()}]\n{v}")
