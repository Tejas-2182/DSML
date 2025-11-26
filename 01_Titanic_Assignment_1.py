import pandas as pd

# Read CSV
df = pd.read_csv("titanic_synthetic.csv")

# (Optional) also read from XLSX by first writing to xlsx (to demonstrate both formats)
df.to_excel("titanic_synthetic.xlsx", index=False)
df_xlsx = pd.read_excel("titanic_synthetic.xlsx")

# Indexing & selecting
subset_pos = df.iloc[:5, :3]                 # first 5 rows, first 3 cols
subset_named = df.loc[:, ["survived","pclass","sex","age","fare"]]

# Sorting
sorted_by_fare = df.sort_values("fare", ascending=False)

# Describe + types
desc = df.describe(include="all")
dtypes = df.dtypes

print(subset_pos, "\n")
print(subset_named.head(), "\n")
print(sorted_by_fare.head(), "\n")
print(desc, "\n")
print(dtypes)
