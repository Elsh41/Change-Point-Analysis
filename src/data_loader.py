import os
import numpy as np
import pandas as pd

def load_and_preprocess_prices(file_path: str) -> pd.DataFrame:
    """
    Loads Brent oil price CSV, cleans missing dates, and calculates log returns.
    
    Parameters:
        file_path (str): Path to raw CSV file.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame with 'Price' and 'Log_Returns' indexed by Date.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found at: {file_path}")
        
    # Read without parse_dates to avoid automatic format inference warnings
    df = pd.read_csv(file_path)
    
    # Standardize column names
    df.columns = [col.strip().capitalize() for col in df.columns]
    
    if 'Date' not in df.columns or 'Price' not in df.columns:
        raise KeyError("CSV must contain 'Date' and 'Price' columns.")
        
    # Explicit date parsing after loading
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
    df = df.sort_values('Date').drop_duplicates(subset=['Date']).set_index('Date')
    
    # Handle missing trading days cleanly
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Price'] = df['Price'].ffill().bfill()
    
    # Compute Log Returns: R_t = ln(P_t / P_{t-1})
    df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1)).fillna(0.0)
    
    return df