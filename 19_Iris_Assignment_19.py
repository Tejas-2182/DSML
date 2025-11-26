import pandas as pd
iris = pd.read_csv("iris_synthetic.csv")
num = ["sepal_length","sepal_width","petal_length","petal_width"]

print("Mean/Std:\n", iris.groupby("species")[num].agg(["mean","std"]))
print("\nPercentiles (0.25,0.5,0.75):\n",
      iris.groupby("species")[num].quantile([0.25,0.5,0.75]).unstack(level=-1))
