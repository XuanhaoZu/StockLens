
import requests
from datetime import datetime, timedelta
from langchain_core.tools import tool
from pprint import pprint

API_KEY = '5280A66MWDO73OD0'
BASE_URL = 'https://www.alphavantage.co/query'

@tool
def fetch_stock_data(symbol, horizon: int) -> dict:
    """Fetch stock data for a given symbol and horizon.
    
    Args:
        symbol: The stock symbol to fetch data for.
        horizon: The number of months to look back.
    """
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }
    
    response = requests.get(BASE_URL, params=parameters)
    data = response.json()

    if 'Time Series (Daily)' not in data:
        return "Unable to get time series data."
        
    ts_data = data['Time Series (Daily)']
    
    start_time = datetime.now() - timedelta(days=30 * horizon)
    
    # Create a new dictionary containing only the last 365 days
    filtered_dict = {}
    for date_str, daily_metrics in ts_data.items():
        # Convert the string key (e.g., '2024-10-24') to a datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Keep the data if it falls within the last year
        if date_obj >= start_time:
            filtered_dict[date_str] = daily_metrics
            
    return filtered_dict

if __name__ == '__main__':
    output = fetch_stock_data.invoke({
        "symbol": "AAPL",
        "horizon": 1
    })
    pprint(output)