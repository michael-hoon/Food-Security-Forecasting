"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd
from pandas import DataFrame
import app.model as model

def create_dataframe() -> DataFrame:
    """Create Pandas DataFrame from local CSV."""
    predictors = model.predictors
    country = model.country
    df = pd.read_excel("data/2Ddataset.xlsx")
    return df
