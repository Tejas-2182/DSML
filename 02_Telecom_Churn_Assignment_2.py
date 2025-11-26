import pandas as pd

df = pd.read_csv("telecom_churn_synthetic.csv")

summary = {}

for col in df.columns:
    s = df[col]

    if pd.api.types.is_numeric_dtype(s):
        summary[col] = {
            "min": s.min(),
            "max": s.max(),
            "mean": s.mean(),
            "std": s.std(),
            "var": s.var(),
            "25%": s.quantile(0.25),
            "50%": s.quantile(0.5),
            "75%": s.quantile(0.75)
        }
    else:
        summary[col] = {
            "unique values": s.nunique(),
            "most frequent": s.mode()[0]
        }

summary_df = pd.DataFrame(summary).T
print(summary_df)
