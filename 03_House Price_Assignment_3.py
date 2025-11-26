import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("house_price_synthetic.csv")

numeric = df.select_dtypes(include=[np.number]).columns.tolist()
print('Numeric features:', numeric)

for col in numeric:
    coldata = df[col].dropna()
    print(f'Feature: {col} -> std: {coldata.std()}, var: {coldata.var()}, 25%:{coldata.quantile(0.25)}, 50%: {coldata.median()}, 75%: {coldata.quantile(0.75)}')
    plt.figure()
    plt.hist(coldata, bins=20)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    # plt.show()  # In script, show or save as needed
