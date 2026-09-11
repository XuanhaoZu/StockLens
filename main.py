from datetime import date
from pprint import pprint

from state import create_initial_state
from graph import build_graph
from dotenv import load_dotenv

load_dotenv()

def main() -> None:
    ticker = input("Enter a stock ticker: ").strip().upper()
    if not ticker:
        print("Ticker cannot be empty. Please run the program again.")
        return

    # 研究使用的周期
    horizon = input("Research horizon (default: 1-5 months): ").strip()
    horizon = 2 # fix

    # create state
    state = create_initial_state(
        ticker=ticker,                 
        horizon=horizon
    )

    graph = build_graph()

    result = graph.invoke(state)


    print("\nResearch state after graph execution:")
    pprint(result, sort_dicts=False)



if __name__ == "__main__":
    main()