from langchain_protocol import Any

from state import StockAnalysisState


def risk_gate_node(state: StockAnalysisState) -> dict[str, Any]:
    market_data = state["market_data"]

    if market_data is None:
        reason = "Market data is missing."

    elif market_data.get("is_simulated") is True:
        reason = "Market data is simulated."    

    else:
        reason = "Financial risk rules have not been implemented yet."

    return {
            "risk": {
                "status": "not_evaluated",
                "reasons": [reason],
            }
    }