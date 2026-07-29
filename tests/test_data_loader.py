import pytest
import pandas as pd
import numpy as np
import os
from src.data_loader import load_and_preprocess_prices

@pytest.fixture
def sample_csv(tmp_path):
    """Creates a temporary sample Brent price CSV file for testing."""
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test_brent.csv"
    
    dates = pd.date_range(start="2024-01-01", periods=5, freq="D")
    prices = [75.0, 77.0, 76.5, 80.0, 79.0]
    
    df = pd.DataFrame({"Date": dates, "Price": prices})
    df.to_csv(p, index=False)
    return str(p)

def test_load_and_preprocess_prices_structure(sample_csv):
    df = load_and_preprocess_prices(sample_csv)
    
    assert isinstance(df, pd.DataFrame)
    assert "Price" in df.columns
    assert "Log_Returns" in df.columns
    assert len(df) == 5
    assert isinstance(df.index, pd.DatetimeIndex)

def test_log_returns_calculation(sample_csv):
    df = load_and_preprocess_prices(sample_csv)
    
    # Verify R_1 = ln(77.0 / 75.0)
    expected_return_1 = np.log(77.0 / 75.0)
    assert np.isclose(df['Log_Returns'].iloc[1], expected_return_1)

def test_missing_file_raises_error():
    with pytest.raises(FileNotFoundError):
        load_and_preprocess_prices("non_existent_file.csv")