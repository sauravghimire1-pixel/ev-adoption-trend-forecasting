import pandas as pd
import numpy as np


def drop_duplicates_and_nulls(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Drop duplicate rows and columns with more than `threshold` missing values."""
    df = df.drop_duplicates()
    null_frac = df.isnull().mean()
    df = df.loc[:, null_frac < threshold]
    return df


def fill_missing(df: pd.DataFrame, strategy: str = "median") -> pd.DataFrame:
    """Fill missing numeric values using mean or median."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if strategy == "median":
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mean())
    return df


def standardize_region(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Lowercase and strip whitespace from a region/country column."""
    df[col] = df[col].str.strip().str.lower()
    return df


def filter_years(df: pd.DataFrame, year_col: str, start: int, end: int) -> pd.DataFrame:
    """Filter dataframe to a range of years."""
    return df[(df[year_col] >= start) & (df[year_col] <= end)].copy()
