import pandas as pd

df = pd.read_csv("titanic_synthetic.csv")

print('Unique counts per column:')
print(df.nunique())
print('\nColumn dtypes:')
print(df.dtypes)
# Convert a column dtype example (if numeric stored as object)
for col in df.columns:
    if df[col].dtype == object:
        try:
            df[col] = pd.to_numeric(df[col])
            print(f'Converted {col} to numeric')
        except:
            pass
# Missing values
print('\nMissing values per column:')
print(df.isna().sum())
# Fill missing values: numeric -> mean, object -> mode
for col in df.columns:
    if df[col].isna().sum()>0:
        if df[col].dtype in [np.float64, np.int64]:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna(df[col].mode().iloc[0] if not df[col].mode().empty else 'Unknown', inplace=True)
print('\nAfter filling, missing values per column:')
print(df.isna().sum())
