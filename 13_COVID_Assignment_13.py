import pandas as pd

df = pd.read_csv("covid_vaccine_synthetic.csv")
print(df.describe(include="all"))

statewise = df.groupby("State", dropna=False)[["FirstDose","SecondDose"]].sum().sort_values("FirstDose", ascending=False)
print(statewise)
