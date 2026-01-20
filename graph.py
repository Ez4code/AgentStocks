# MarketContext → WaveAnalysis → END
from langgraph.graph import StateGraph, END
from state import AgentState
from agents.wave_analysis import market_context_node, wave_analysis_node

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("market_context", market_context_node)
    graph.add_node("wave_analysis", wave_analysis_node)

    graph.set_entry_point("market_context")
    graph.add_edge("market_context", "wave_analysis")
    graph.add_edge("wave_analysis", END)

    return graph.compile()
