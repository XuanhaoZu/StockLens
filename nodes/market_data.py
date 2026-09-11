from typing import Any

from state import StockAnalysisState


def market_data_node(state: StockAnalysisState) -> dict[str, Any]:
    ticker = state["ticker"]

    market_data = {
        "ticker": ticker,
        "source": "synthetic_demo",
        "is_simulated": True,
        "currency": "USD",
        "price": 100.0,
        "volume": 1000000,
        }

    return {
        "market_data": market_data,
    }
