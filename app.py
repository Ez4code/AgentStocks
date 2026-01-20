from graph import build_graph

def main():
    graph = build_graph()

    stock_name = "合盛硅业"

    init_state = {
        "stock_name": stock_name,
        "kline_data": {},
        "wave_analysis": "",
        "up_prob": 0.0,
        "down_prob": 0.0
    }

    result = graph.invoke(init_state)

    print("\n==== 波浪分析结果 ====\n")
    print(result["wave_analysis"])
    print(f"\n上涨概率: {result['up_prob']:.2f}")
    print(f"下跌概率: {result['down_prob']:.2f}")

if __name__ == "__main__":
    main()
