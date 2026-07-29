# Brent Crude Oil Price Analysis & Change Point Detection

## Project Overview
This project analyzes historical Brent crude oil prices to detect structural breaks, evaluate the statistical impact of major macroeconomic/geopolitical events, and prepare regime-aware time series models (ARIMA/GARCH).

## Dataset Sourcing
* **Brent Oil Prices (`data/raw/brent_prices.csv`):** Daily historical closing prices sourced from the U.S. Energy Information Administration (EIA) / World Bank Commodity Markets data, covering daily prices in USD per barrel.
* **Events Dataset (`data/processed/oil_events.csv`):** A curated tabular dataset of 13 key OPEC decisions, geopolitical conflicts, and economic shocks spanning 1990–2026.

## Environment & Setup Nuances
1. **Python Version:** Python 3.9+ is recommended.
2. **Virtual Environment Setup:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt