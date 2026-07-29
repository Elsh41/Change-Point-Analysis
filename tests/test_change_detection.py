import pytest
import pandas as pd
import numpy as np
from src.change_detection import detect_structural_breaks

@pytest.fixture
def synthetic_step_series():
    """Generates a synthetic time series with a clear mean shift at day 50."""
    np.random.seed(42)
    dates = pd.date_range(start="2024-01-01", periods=100, freq="D")
    part1 = np.random.normal(loc=50, scale=1.0, size=50)
    part2 = np.random.normal(loc=100, scale=1.0, size=50)
    series = pd.Series(np.concatenate([part1, part2]), index=dates)
    return series

def test_detect_structural_breaks(synthetic_step_series):
    breaks = detect_structural_breaks(synthetic_step_series, model="l2", penalty=5.0)
    
    assert isinstance(breaks, list)
    assert len(breaks) > 0
    # Break should be detected near 2024-02-19 (index 49/50)
    assert any(abs((b - pd.Timestamp("2024-02-19")).days) <= 3 for b in breaks)

def test_short_series_raises_error():
    short_series = pd.Series([10.0, 12.0, 11.0], index=pd.date_range("2024-01-01", periods=3))
    with pytest.raises(ValueError):
        detect_structural_breaks(short_series)