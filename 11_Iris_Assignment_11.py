import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris_synthetic.csv")
print("Dtypes:\n", iris.dtypes)

for c in ["sepal_length","sepal_width","petal_length","petal_width"]:
    plt.figure()
    iris[c].hist(bins=20)
    plt.title(f"Histogram: {c}")
    plt.xlabel(c); plt.ylabel("count")
    plt.show()
