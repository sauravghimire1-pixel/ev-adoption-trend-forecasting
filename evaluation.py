import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_forecast(y_true, y_pred) -> dict:
    """Return MAE, RMSE, R², and MAPE for a forecasting model."""
    mape = np.mean(np.abs((y_true - y_pred) / np.where(y_true == 0, 1, y_true))) * 100
    return {
        "MAE": round(mean_absolute_error(y_true, y_pred), 4),
        "RMSE": round(np.sqrt(mean_squared_error(y_true, y_pred)), 4),
        "R2": round(r2_score(y_true, y_pred), 4),
        "MAPE (%)": round(mape, 2),
    }


def print_metrics(metrics: dict) -> None:
    for k, v in metrics.items():
        print(f"  {k}: {v}")
