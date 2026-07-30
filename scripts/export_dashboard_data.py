import os
import json
import pandas as pd

# Define output directory relative to project root
out_dir = os.path.join("dashboard", "backend", "data")
os.makedirs(out_dir, exist_ok=True)

# 1. Export Brent Prices
prices_path = os.path.join("data", "raw", "BrentOilPrices.csv")
if os.path.exists(prices_path):
    df_prices = pd.read_csv(prices_path)
    df_prices.columns = [col.strip().capitalize() for col in df_prices.columns]
    
    # Convert to datetime and clean
    df_prices['Date'] = pd.to_datetime(df_prices['Date'], format='mixed', errors='coerce')
    df_prices = df_prices.dropna(subset=['Date', 'Price']).sort_values('Date')
    
    # IMPORTANT FIX: Convert Date to string before to_dict()
    df_prices['date'] = df_prices['Date'].dt.strftime('%Y-%m-%d')
    df_prices = df_prices.rename(columns={'Price': 'price'})
    
    # Select only plain python serializable columns
    prices_json = df_prices[['date', 'price']].to_dict(orient='records')

    with open(os.path.join(out_dir, "brent_prices.json"), "w") as f:
        json.dump(prices_json, f, indent=2)
    print(f"✅ Exported {len(prices_json)} price records to brent_prices.json")
else:
    print(f"❌ File not found: {prices_path}")

# 2. Export Oil Events
events_path = os.path.join("data", "processed", "oil_events.csv")
if os.path.exists(events_path):
    df_events = pd.read_csv(events_path)
    events_json = df_events.to_dict(orient='records')
    with open(os.path.join(out_dir, "oil_events.json"), "w") as f:
        json.dump(events_json, f, indent=2)
    print(f"✅ Exported {len(events_json)} events to oil_events.json")
else:
    fallback_events = [
        {"Date": "2014-11-27", "Event_Name": "OPEC Non-Cut Decision", "Category": "OPEC Decision"},
        {"Date": "2020-03-09", "Event_Name": "Saudi-Russia Price War / COVID crash", "Category": "Price War / Pandemic"},
        {"Date": "2022-02-24", "Event_Name": "Russia-Ukraine War Invasion", "Category": "Armed Conflict"}
    ]
    with open(os.path.join(out_dir, "oil_events.json"), "w") as f:
        json.dump(fallback_events, f, indent=2)
    print("⚠️ Used fallback events catalog for oil_events.json")

# 3. Export Change Points (Task 2 PyMC Results)
change_points_data = [
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
with open(os.path.join(out_dir, "change_points.json"), "w") as f:
    json.dump(change_points_data, f, indent=2)
print("✅ Exported change_points.json")

print("\n🎉 All dashboard datasets successfully written!")