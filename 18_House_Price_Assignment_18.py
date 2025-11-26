import pandas as pd
df = pd.read_csv("house_price_synthetic.csv")

# Create a categorical "QualityBand" from OverallQual
bins = [0,3,6,10]; labels=["Low","Med","High"]
df["QualityBand"] = pd.cut(df["OverallQual"], bins=bins, labels=labels, include_lowest=True)

summary = df.groupby("QualityBand")["SalePrice"].agg(["count","mean","median","min","max","std"])
print(summary)
