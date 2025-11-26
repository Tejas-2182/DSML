import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("house_price_synthetic.csv")
num_cols = df.select_dtypes(include=np.number).columns

# stats
out = []
for c in num_cols:
    s = df[c].dropna()
    out.append({"feature": c, "std": s.std(), "var": s.var(),
                "p25": s.quantile(0.25), "p50": s.quantile(0.5), "p75": s.quantile(0.75)})
print(pd.DataFrame(out))

# histograms
for c in num_cols:
    plt.figure()
    df[c].hist(bins=30)
    plt.title(f"Histogram: {c}")
    plt.xlabel(c); plt.ylabel("count")
    plt.show()
