import math, pandas as pd
df = pd.read_csv("cosmetics_synthetic.csv")

def entropy(y):
    p = y.value_counts(normalize=True)
    return -sum(pi*math.log2(pi) for pi in p if pi>0)

def info_gain(df, feature, target="Buys"):
    base = entropy(df[target])
    cond = sum((len(v)/len(df)) * entropy(v[target]) for _, v in df.groupby(feature))
    return base - cond

target = "Buys"
features = [c for c in df.columns if c != target]
gains = {f: info_gain(df, f, target) for f in features}
root = max(gains, key=gains.get)
print("Information Gain:", gains)
print("Root node:", root)
