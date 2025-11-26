import pandas as pd
import numpy as np

df = pd.read_csv('telecom_churn_synthetic.csv')
print('Loaded shape', df.shape)
# For each numeric column compute min, max, mean, range, std, var, percentiles
numeric = df.select_dtypes(include=[np.number]).columns.tolist()
print('Numeric columns:', numeric)
stats = {}
for col in numeric:
    coldata = df[col].dropna()
    stats[col] = {
        'min': coldata.min(),
        'max': coldata.max(),
        'mean': coldata.mean(),
        'range': coldata.max() - coldata.min(),
        'std': coldata.std(),
        'var': coldata.var(),
        '25%': coldata.quantile(0.25),
        '50%': coldata.quantile(0.5),
        '75%': coldata.quantile(0.75)
    }
stats_df = pd.DataFrame(stats).T
print(stats_df)
