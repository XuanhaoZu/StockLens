from typing import Any

from state import StockAnalysisState
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# from ..tools import fetch_stock_data
from tools import fetch_stock_data


def market_data_node(state: StockAnalysisState) -> dict[str, Any]:
    ticker = state["ticker"]
    horizon = int(state["research_context"]["horizon"])

    if horizon <= 0:
        return {
            "error": "Invalid horizon."
        }    

    stock_data = fetch_stock_data.invoke({
        "symbol": ticker,
        "horizon": horizon
    })

    # market_data = {
    #     "ticker": ticker,
    #     "source": "synthetic_demo",
    #     "is_simulated": True,
    #     "currency": "USD",
    #     "price": 100.0,
    #     "volume": 1000000,
    #     }

    return {
        "market_data": stock_data,
    }
