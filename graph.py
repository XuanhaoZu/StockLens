from langgraph.graph import END, START, StateGraph

from nodes.classifier import classifier_node
from nodes.investment_analysis import investment_analysis_node
from nodes.market_data import market_data_node

from nodes.risk_gate import risk_gate_node
from nodes.trading_analysis import trading_analysis_node
from state import StockAnalysisState

def route_opportunity(state: StockAnalysisState) -> str:
    route=state["opportunity_type"]

    if route is None:
        raise ValueError("Opportunity type must be set before routing.")
    
    return route

def build_graph():
    builder = StateGraph(StockAnalysisState)

    # first node(name, function)
    builder.add_node("fetch_market_data", market_data_node)
    builder.add_node("classifier_opportunity", classifier_node)
    builder.add_node("analyze_investment",investment_analysis_node)
    builder.add_node("analyze_trade", trading_analysis_node)
    builder.add_node("check_risk", risk_gate_node)

    builder.add_edge(START, "fetch_market_data")
    builder.add_edge("fetch_market_data", "classifier_opportunity")

    builder.add_conditional_edges(
        "classifier_opportunity",
        route_opportunity,
        {
            "investment": "analyze_investment",
            "trade": "analyze_trade", 
            "need_more": END,
            "reject": END,
        },
    )

    builder.add_edge("analyze_investment", "check_risk")
    builder.add_edge("analyze_trade", "check_risk")
    builder.add_edge("check_risk", END)

    return builder.compile()
    