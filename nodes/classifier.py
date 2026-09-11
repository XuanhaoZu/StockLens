from typing import Any

from state import StockAnalysisState


def classifier_node(state: StockAnalysisState) -> dict[str, Any]:
    if state["market_data"] is None:
        return {
            "opportunity_type": "need_more",
            "routing_reason": "Market data is missing.",
        }

    horizon = state["research_context"]["horizon"].strip().lower()    
    if horizon == "1-3 years":
        return {
            "opportunity_type": "investment",
            "routing_reason": "Demo routing: a long-term research horizon.",        }
    if horizon == "1-4 weeks":
        return {
                "opportunity_type": "trade",
                "routing_reason": "Demo routing: a short-term research horizon.",
        }
    return {
        "opportunity_type": "need_more",
        "routing_reason": "Specify a supported research horizon for this demo.",
    }