from core import AIAnalyst
from config import CONFIG


ai = AIAnalyst(CONFIG)

prompt = "用一句话解释什么是流水线CPU"

# 单模型
print(ai.chat("qwen", prompt))

# 多模型对比
# results = ai.compare(prompt)
# for k, v in results.items():
#     print(f"\n[{k.upper()}]\n{v}")
