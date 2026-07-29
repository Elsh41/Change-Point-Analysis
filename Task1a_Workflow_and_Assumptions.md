# Task 1a: Analysis Workflow, Assumptions, and Limitations

## 1. Concise End-to-End Analysis Workflow

1. **Data Ingestion & Cleaning:** Load daily raw Brent prices, sort chronologically, reindex continuous calendar days, and fill weekend/holiday gaps via forward-filling (`ffill()`).
2. **Feature Engineering:** Calculate Daily Log Returns $R_t = \ln(P_t / P_{t-1})$ and rolling volatility metrics to stabilize non-stationary price variance.
3. **Diagnostic Time Series Analysis:**
   * Evaluate trend via visual decomposition (STL).
   * Conduct Augmented Dickey-Fuller (ADF) tests on raw prices vs. log returns.
   * Test for ARCH effects to confirm volatility clustering.
4. **Structural Change Point Detection:** Execute Binary Segmentation (`Binseg` with $L_2$ cost) on price and return series using the `ruptures` library to extract structural break timestamps.
5. **Event Alignment:** Overlay detected change dates onto the pre-compiled `oil_events.csv` dataset using a temporal window ($\pm 14$ days) to evaluate historical co-occurrence.
6. **Regime-Aware Modeling & Insights:** Fit piecewise ARIMA-GARCH models across identified regimes, quantifying parameter shifts and generating actionable risk insights.

---

## 2. Assumptions and Limitations

### Analytical Assumptions
* **Semi-Strong Market Efficiency:** Asset prices rapidly incorporate all publicly available macroeconomic and geopolitical information.
* **Continuity of Price Series:** Forward-filling non-trading days accurately preserves the underlying economic state without introducing artificial returns.

### Limitations & Critical Distinction: Correlation vs. Causal Impact
* **Co-occurrence in Time is Not Causality:** Finding that a change point occurred on `2022-02-24` alongside the invasion of Ukraine demonstrates **temporal association**, not statistical causality.
* **Confounding Variables & Omitted Variable Bias:** Oil prices respond simultaneously to interest rate adjustments, US dollar index ($\text{DXY}$) swings, maritime freight rates, and commercial inventory levels. Attributing a price shift entirely to a headline event without controlling for exogenous market variables risks severe omitted variable bias.
* **Resolution Bottlenecks:** Daily closing prices cannot isolate intra-day high-frequency reactions to real-time press briefings or emergency OPEC announcements.