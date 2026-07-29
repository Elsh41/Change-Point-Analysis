import pandas as pd
import json

# 1. Prices
df_prices = pd.read_csv("data/raw/BrentOilPrices.csv")
df_prices['Date'] = pd.to_datetime(df_prices['Date'])
df_prices = df_prices.sort_values('Date').dropna()
prices_json = df_prices.rename(columns={'Date': 'date', 'Price': 'price'}).to_dict(orient='records')

with open("dashboard/backend/data/brent_prices.json", "w") as f:
    json.dump(prices_json, f)

# 2. Events
df_events = pd.read_csv("data/processed/oil_events.csv")
events_json = df_events.to_dict(orient='records')
with open("dashboard/backend/data/oil_events.json", "w") as f:
    json.dump(events_json, f)

# 3. Change Points (Task 2 PyMC Model Summary)
change_points_json = [
    {
        "id": "cp_2014",
        "date": "2014-11-26",
        "event_name": "OPEC Non-Cut Decision",
        "category": "OPEC Decision",
        "pre_mean": 105.77,
        "post_mean": 48.69,
        "pct_change": -53.96,
        "hdi_95": ["2014-11-22", "2014-11-28"]
    }
]
with open("dashboard/backend/data/change_points.json", "w") as f:
    json.dump(change_points_json, f)

