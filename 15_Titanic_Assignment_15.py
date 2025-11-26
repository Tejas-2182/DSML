import pandas as pd, seaborn as sns, matplotlib.pyplot as plt

t = pd.read_csv("titanic_synthetic.csv")

plt.figure(); sns.countplot(data=t, x="pclass", hue="survived"); plt.title("Survival by Class"); plt.show()
plt.figure(); sns.countplot(data=t, x="sex", hue="survived"); plt.title("Survival by Sex"); plt.show()
plt.figure(); sns.histplot(data=t, x="age", hue="survived", bins=20, element="step"); plt.title("Age vs Survival"); plt.show()
