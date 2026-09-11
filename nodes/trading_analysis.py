def trading_analysis_node(state: dict) -> dict:
    return {
        "trading_analysis": {
            "ticker": state["ticker"],
            "status": "demo_only",
            "summary": "Trading analysis branch executed.",
        }
    }