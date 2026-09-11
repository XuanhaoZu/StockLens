from typing import Any, Literal, TypedDict


class StockAnalysisState(TypedDict):
    ticker: str
    research_context: dict[str, str]

    market_data: dict[str, Any] | None
    news: list[dict[str, Any]] | None

    opportunity_type: Literal[
        "investment", "trade", "need_more", "reject"
    ] | None
    routing_reason: str | None

    investment_analysis: dict[str, Any] | None
    trading_analysis: dict[str, Any] | None

    risk: dict[str, Any] | None
    evidence: dict[str, Any] | None

    research_count: int
    final_strategy: dict[str, Any] | None


def create_initial_state(
        ticker: str,
        horizon: str,
        as_of: str,
) -> StockAnalysisState:
    return {
        "ticker": ticker.strip().upper(),
        "research_context": {
            "horizon": horizon,
            "as_of": as_of,
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