import pandas as pd

df = pd.read_csv("covid_vaccine_synthetic.csv")
print(df.describe(include="all"))

total_male = df["MaleVaccinated"].sum()
total_female = df["FemaleVaccinated"].sum()
print("Total males vaccinated:", int(total_male))
print("Total females vaccinated:", int(total_female))
