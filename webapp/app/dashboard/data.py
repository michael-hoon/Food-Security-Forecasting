"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd
from pandas import DataFrame


def create_dataframe() -> DataFrame:
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_excel("data/2Ddataset.xlsx")
    return df
