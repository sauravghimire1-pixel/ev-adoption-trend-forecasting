# EV Adoption Trend Analysis & Forecasting

Analysis of electric vehicle adoption patterns across regions and time, with forecasting models to project future adoption under multiple scenarios.

## Project Overview

This project examines how policy incentives, charging infrastructure, vehicle pricing, and macroeconomic factors drive EV adoption — and builds a forecasting model to project 3–5 year adoption trajectories.

## Dataset

| Source | Description |
|--------|-------------|
| [IEA Global EV Data Explorer](https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer) | EV registrations by country/year |
| [US Dept. of Energy — AFDC](https://afdc.energy.gov/data/) | US EV sales, charging stations, incentives |
| [Kaggle — EV Dataset](https://www.kaggle.com/datasets) | Supplementary regional EV data |

> **Note:** Raw data files are not committed to this repo. Download sources above and place in `data/raw/`.

## Project Structure

```
ev-adoption-forecasting/
├── data/
│   ├── raw/              # Source data (gitignored)
│   └── processed/        # Cleaned, feature-engineered data
├── notebooks/
│   ├── 01_eda.ipynb          # Exploratory data analysis
│   ├── 02_features.ipynb     # Feature engineering & trend analysis
│   ├── 03_forecasting.ipynb  # Forecasting models & scenarios
│   └── 04_insights.ipynb     # Final insights & visualizations
├── src/
│   ├── preprocessing.py      # Data cleaning utilities
│   ├── features.py           # Feature engineering helpers
│   └── evaluation.py         # Forecasting evaluation metrics
├── reports/
│   └── final_report.pdf
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/yourusername/ev-adoption-forecasting.git
cd ev-adoption-forecasting
pip install -r requirements.txt
jupyter notebook notebooks/01_eda.ipynb
```

## Phases

| Phase | Focus | Milestone |
|-------|-------|-----------|
| 1 | Data collection & EDA | Clean dataset + baseline adoption stats by region |
| 2 | Feature engineering | Feature matrix + key trend patterns identified |
| 3 | Forecasting & modelling | Best model selected, scenario forecasts generated |
| 4 | Insights & presentation | Final report + forecast visualizations |

## Scenarios

The forecasting phase produces three adoption paths:

- **Optimistic** — aggressive incentives, rapid infrastructure growth
- **Base** — continuation of current policy and market trends
- **Pessimistic** — incentive rollbacks, slow charging expansion

## Results

_To be updated after modelling is complete._

## Tech Stack

Python · pandas · scikit-learn · XGBoost · Prophet · matplotlib · seaborn · Jupyter

## Author

Your Name — [GitHub](https://github.com/yourusername)
