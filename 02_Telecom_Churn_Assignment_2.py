import pandas as pd
import numpy as np

df = pd.read_csv("telecom_churn_synthetic.csv")

def stats_for_series(s: pd.Series):
    if pd.api.types.is_numeric_dtype(s):
        return {
            "min": s.min(),
            "max": s.max(),
            "mean": s.mean(),
            "range": s.max() - s.min(),
            "std": s.std(ddof=1),
            "var": s.var(ddof=1),
            "p25": s.quantile(0.25),
            "p50": s.quantile(0.5),
            "p75": s.quantile(0.75),
        }
    return {"unique": s.nunique(), "top": s.mode().iloc[0] if not s.mode().empty else None}

summary = pd.DataFrame({c: stats_for_series(df[c]) for c in df.columns}).T
print(summary)
