import pandas as pd, matplotlib.pyplot as plt

iris = pd.read_csv("iris_synthetic.csv")
num_cols = ["sepal_length","sepal_width","petal_length","petal_width"]

for c in num_cols:
    plt.figure()
    iris.boxplot(column=c)
    plt.title(f"Boxplot: {c}")
    plt.show()

def outliers_iqr(s):
    q1,q3 = s.quantile([0.25,0.75]); iqr = q3-q1
    lo, hi = q1-1.5*iqr, q3+1.5*iqr
    return ((s<lo)|(s>hi)).sum()

print({c: outliers_iqr(iris[c]) for c in num_cols})
