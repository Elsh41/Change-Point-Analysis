import os
import pandas as pd

def generate_event_dataset(output_path="data/processed/oil_events.csv"):
    """Generates a structured CSV of key geopolitical/economic events affecting Brent crude."""
    events = {
        "Date": [
            "1990-08-02", "2001-09-11", "2003-03-20", "2008-09-15", 
            "2011-02-15", "2014-11-27", "2018-11-05", "2020-03-08", 
            "2020-03-11", "2022-02-24", "2023-10-07", "2024-01-12", "2026-01-01"
        ],
        "Event_Name": [
            "Invasion of Kuwait", "9/11 Terrorist Attacks", "US Invasion of Iraq", "Lehman Brothers Bankruptcy",
            "Libyan Civil War Begins", "OPEC Non-Cut Decision", "US Re-imposition of Iran Sanctions", "Saudi-Russia Price War",
            "WHO Declares COVID-19 Pandemic", "Russia Invades Ukraine", "Israel-Hamas War Begins", "US/UK Red Sea Airstrikes", "OPEC+ Supply Cut Extensions"
        ],
        "Category": [
            "Geopolitical/War", "Geopolitical/Security", "Geopolitical/War", "Economic Shock",
            "Geopolitical/Civil War", "OPEC Decision", "Geopolitical/Sanctions", "OPEC/Market Share War",
            "Economic/Global Health", "Geopolitical/War", "Geopolitical/War", "Geopolitical/Shipping", "OPEC Decision"
        ],
        "Expected_Market_Impact": [
            "Supply disruption fears; sharp price spike.",
            "Aviation/demand crash; initial price drop.",
            "Supply disruptions; oil price volatility.",
            "Global financial crisis; severe demand collapse.",
            "Libyan production halt; supply-driven price spike.",
            "OPEC refuses to cut production; massive supply glut & price crash.",
            "Iranian supply restriction; price upward pressure.",
            "Failed production cuts; catastrophic price crash.",
            "Global lockdowns; demand destruction & negative oil pricing futures.",
            "Sanctions on Russian energy; severe price spike.",
            "Middle East instability fears; moderate risk premium added.",
            "Houthi shipping disruption; transit delays & price spikes.",
            "Extended production cuts to support floor price."
        ]
    }
    
    df = pd.DataFrame(events)
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Dataset compiled and saved to {output_path}")

if __name__ == "__main__":
    generate_event_dataset()


def load_and_preprocess_prices(file_path):
    """Loads Brent oil prices, handles missing dates, and returns prices and log returns."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The target dataset at {file_path} was not found. Please verify paths.")
    
    try:
        # Load data
        df = pd.read_csv(file_path, parse_dates=['Date'])
        df = df.sort_values('Date').set_index('Date')
        
        # Keep only the target price column (assuming column name is 'Price')
        if 'Price' not in df.columns:
            # Fallback to identify pricing column if named differently
            df = df.rename(columns={df.columns[0]: 'Price'})
            
        # Clean missing values using forward fill (handles weekends/holidays)
        df['Price'] = df['Price'].ffill().bfill()
        
        # Calculate Log Returns
        # Formula: R_t = ln(P_t / P_{t-1})
        import numpy as np
        df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1))
        df['Log_Returns'] = df['Log_Returns'].fillna(0)
        
        return df
    except Exception as e:
        raise ValueError(f"Error parsing the price dataset: {str(e)}")