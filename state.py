from typing import Any, Literal, TypedDict, Dict, List, Optional


class StockAnalysisState(TypedDict):
    ticker: str
    research_context: Dict[str, int]

    market_data: Optional[Dict[str, Any]]
    news: Optional[List[Dict[str, Any]]]

    opportunity_type: Optional[Literal[
        "investment", "trade", "need_more", "reject"
    ]]
    routing_reason: Optional[str]

    investment_analysis: Optional[Dict[str, Any]]
    trading_analysis: Optional[Dict[str, Any]]

    risk: Optional[Dict[str, Any]]
    evidence: Optional[Dict[str, Any]]

    research_count: int
    final_strategy: Optional[Dict[str, Any]]
    error: Optional[str]


def create_initial_state(
        ticker: str,
        horizon: int
) -> StockAnalysisState:
    return {
        "ticker": ticker.strip().upper(),
        "research_context": {
            "horizon": horizon
        },
        "market_data": None,
        "news": None,
        "opportunity_type": None,
        "routing_reason": None,
        "investment_analysis": None,
        "trading_analysis": None,
        "risk": None,
        "evidence": None,
        "research_count": 0,
        "final_strategy": None,
    }