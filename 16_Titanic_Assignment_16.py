import pandas as pd, matplotlib.pyplot as plt

t = pd.read_csv("titanic_synthetic.csv")
t["fare"].hist(bins=30)
plt.title("Fare Distribution"); plt.xlabel("fare"); plt.ylabel("count")
plt.show()
