import pandas as pd, math
df = pd.read_csv("cosmetics_synthetic.csv")

def entropy(y):
    p = y.value_counts(normalize=True)
    return -sum(pi*math.log2(pi) for pi in p if pi>0)

freq = df["Age"].value_counts()
print("Frequency Age:\n", freq)

base = entropy(df["Buys"])
weighted = sum((len(g)/len(df))*entropy(g["Buys"]) for _, g in df.groupby("Age"))
print("Information Gain (Age):", base - weighted)
