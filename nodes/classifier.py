from typing import Any, Literal
from state import StockAnalysisState
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage

PROJ_PATH = os.path.dirname(os.path.dirname(__file__))

env_path = os.path.join(PROJ_PATH, ".env")
# print("env_path=", env_path)
load_dotenv(env_path)

assert os.environ.get("OPENAI_API_KEY"), "OPENAI_API_KEY not found"

CLASSIFICATION_PROMPT = """
Based on the stock data, recommend user the next step. 
The next step can only be 'need_more', 'investment' or 'trade'.
Also give the reason based on your recommendation.

The stock data is listed as follows:
{STOCK_DATA}
"""

llm = ChatOpenAI(model="gpt-4o", temperature=0)

class MarketDataClassifierModel(BaseModel):
    """Classify based on given stock data"""
    opportunity_type: Literal["need_more", "investment", "trade"] = Field(description="The recommended action for this current stock.")
    routing_reason: str = Field(description="The reason for the recommended action.")


def classifier_node(state: StockAnalysisState) -> dict[str, Any]:
    if state["market_data"] is None:
        return {
            "opportunity_type": "need_more",
            "routing_reason": "Market data is missing.",
        }
    llm_classifier = llm.with_structured_output(MarketDataClassifierModel)
    resp = llm_classifier.invoke([
        HumanMessage(content=CLASSIFICATION_PROMPT.format(STOCK_DATA=state["market_data"]))
    ])
    print("CLS RESP:", resp)
    return resp.model_dump()

    

# def classifier_node(state: StockAnalysisState) -> dict[str, Any]:
#     if state["market_data"] is None:
#         return {
#             "opportunity_type": "need_more",
#             "routing_reason": "Market data is missing.",
#         }

#     horizon = state["research_context"]["horizon"].strip().lower()    
#     if horizon == "1-3 years":
#         return {
#             "opportunity_type": "investment",
#             "routing_reason": "Demo routing: a long-term research horizon.",        }
#     if horizon == "1-4 weeks":
#         return {
#                 "opportunity_type": "trade",
#                 "routing_reason": "Demo routing: a short-term research horizon.",
#         }
#     return {
#         "opportunity_type": "need_more",
#         "routing_reason": "Specify a supported research horizon for this demo.",
#     }