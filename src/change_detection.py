import numpy as np
import ruptures as rpt

def detect_structural_breaks(prices_series, penalty=10):
    """
    Detects structural breaks in the mean and variance of a price series using 
    the Binary Segmentation algorithm from the ruptures library.
    
    Parameters:
    - prices_series (pd.Series): The pricing/returns series to analyze.
    - penalty (int): Penalty value to prevent over-segmentation.
    
    Returns:
    - list: List of timestamps indicating change points.
    """
    if len(prices_series) < 10:
        raise ValueError("Time series data is too short to perform change point analysis.")
        
    # Convert series to numpy array
    signal = prices_series.values
    
    # Initialize Binary Segmentation model (using L2 norm for mean shifts)
    algo = rpt.Binseg(model="l2").fit(signal)
    
    try:
        # Predict change point indices
        result_indices = algo.predict(pen=penalty)
        
        # Map indices back to index dates (excluding the last end-of-series indicator)
        change_dates = [prices_series.index[idx - 1] for idx in result_indices[:-1]]
        return change_dates
    except Exception as e:
        print(f"Error during change point estimation: {str(e)}")
        return []