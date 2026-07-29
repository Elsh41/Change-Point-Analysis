import pandas as pd
import ruptures as rpt

def detect_structural_breaks(series: pd.Series, model: str = "l2", penalty: float = 10.0) -> list:
    """
    Detects structural change points in a time series using Binary Segmentation.
    
    Parameters:
        series (pd.Series): Time series indexed by DatetimeIndex.
        model (str): Ruptures cost model ('l2', 'l1', 'rbf').
        penalty (float): Penalty coefficient governing penalty for adding breakpoints.
        
    Returns:
        list: List of pd.Timestamp objects corresponding to structural change dates.
    """
    if len(series) < 10:
        raise ValueError("Series length must be at least 10 observations for change detection.")
        
    signal = series.values.reshape(-1, 1)
    algo = rpt.Binseg(model=model).fit(signal)
    
    # Predict breakpoint indices
    breakpoint_indices = algo.predict(pen=penalty)
    
    # Map array indices back to DatetimeIndex
    change_dates = []
    for idx in breakpoint_indices[:-1]:  # Exclude the final length index
        # Cap index at boundary
        safe_idx = min(idx - 1, len(series) - 1)
        change_dates.append(series.index[safe_idx])
        
    return change_dates