import pandas as pd
df = pd.read_csv("titanic_synthetic.csv")

# Counting unique values
unique_counts = df.nunique()

# Format / dtype of each column
dtypes = df.dtypes

# Example conversions: 'pclass' to int16, 'survived' to int8
df["pclass"] = df["pclass"].astype("int16")
df["survived"] = df["survived"].astype("int8")

# Identify missing values (inject an example)
df.loc[0,"age"] = None
missing_before = df.isna().sum()

# Fill missing: numeric -> median; categorical -> mode
for c in df.columns:
    if pd.api.types.is_numeric_dtype(df[c]):
        df[c] = df[c].fillna(df[c].median())
    else:
        mode = df[c].mode()
        df[c] = df[c].fillna(mode.iloc[0] if not mode.empty else "Unknown")

missing_after = df.isna().sum()
print(unique_counts, "\n", dtypes, "\n", "Missing before:\n", missing_before, "\nMissing after:\n", missing_after)
