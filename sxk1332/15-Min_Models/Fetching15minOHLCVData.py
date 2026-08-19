import requests
import pandas as pd
from datetime import datetime, timedelta

# Your Market Data API key
API_KEY = "NmsyMmQzMnRXcUVpaGlSM0ptYTNaQlVlQmVoalRuUG5BVktPX3JEeVBkOD0"

# Stock and interval
SYMBOL = "AAPL"
RESOLUTION = 15  # 15 minute resolution

# Date range
START = datetime(2015, 1, 1)
END   = datetime(2026, 1, 9)

def fetch_15min_data(symbol, resolution, start_dt, end_dt, api_key):
    rows = []
    current_start = start_dt

    while current_start < end_dt:
        # Fetch ~30 days per chunk to stay reasonable
        chunk_end = current_start + timedelta(days=30)
        if chunk_end > end_dt:
            chunk_end = end_dt

        url = (
            f"https://api.marketdata.app/v1/stocks/candles/{resolution}/{symbol}"
            f"?from={current_start.strftime('%Y-%m-%d')}"
            f"&to={chunk_end.strftime('%Y-%m-%d')}"
            f"&key={api_key}"
        )

        print(f"Requesting: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
            break

        data = response.json()
        if "t" in data:
            for i in range(len(data["t"])):
                rows.append({
                    "timestamp": pd.to_datetime(data["t"][i], unit="s"),
                    "open": data["o"][i],
                    "high": data["h"][i],
                    "low": data["l"][i],
                    "close": data["c"][i],
                    "volume": data["v"][i],
                })

        current_start = chunk_end + timedelta(days=1)

    df = pd.DataFrame(rows)
    return df

# Fetch and save
df_15min = fetch_15min_data(SYMBOL, RESOLUTION, START, END, API_KEY)
df_15min.to_csv("AAPL_15min_OHLCV.csv", index=False)
print("Saved AAPL_15min_OHLCV.csv")
