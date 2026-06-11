import pandas as pd


def add_time_features(df: pd.DataFrame, year_col: str) -> pd.DataFrame:
    """Add derived time features from a year column."""
    df["decade"] = (df[year_col] // 10) * 10
    df["years_since_2010"] = df[year_col] - 2010
    return df


def add_policy_flag(df: pd.DataFrame, year_col: str, incentive_years: list) -> pd.DataFrame:
    """Flag years where major incentive policies were active."""
    df["incentive_active"] = df[year_col].isin(incentive_years).astype(int)
    return df


def add_scenario_multiplier(df: pd.DataFrame, scenario: str = "base") -> pd.DataFrame:
    """Apply a growth multiplier based on forecast scenario."""
    multipliers = {"optimistic": 1.25, "base": 1.0, "pessimistic": 0.75}
    df["scenario"] = scenario
    df["scenario_multiplier"] = multipliers.get(scenario, 1.0)
    return df


def encode_categoricals(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """One-hot encode categorical columns."""
    return pd.get_dummies(df, columns=cols, drop_first=True)
