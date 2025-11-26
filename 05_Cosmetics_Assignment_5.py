import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("cosmetics_synthetic.csv")
X, y = df.drop(columns=["Buys"]), df["Buys"]
cat = X.columns.tolist()

pipe = Pipeline([
    ("prep", ColumnTransformer([("ohe", OneHotEncoder(handle_unknown="ignore"), cat)])),
    ("clf", DecisionTreeClassifier(random_state=42))
])
pipe.fit(X, y)

test = pd.DataFrame([{"Age":"<21","Income":"Low","Gender":"Female","MaritalStatus":"Married"}])
print("Decision:", pipe.predict(test)[0])
