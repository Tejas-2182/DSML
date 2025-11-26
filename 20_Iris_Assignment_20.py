import pandas as pd, numpy as np
X = pd.read_csv("iris_synthetic.csv")[["sepal_length","sepal_width","petal_length","petal_width"]].to_numpy()

rng = np.random.default_rng(42)
centroids = X[rng.integers(0, len(X), size=3)]

def assign(X, C):
    D = np.linalg.norm(X[:,None,:]-C[None,:,:], axis=2)
    return D.argmin(axis=1)

def update(X, labels, k):
    return np.vstack([X[labels==i].mean(axis=0) for i in range(k)])

for _ in range(10):
    labels = assign(X, centroids)
    newC = update(X, labels, 3)
    if np.allclose(newC, centroids): break
    centroids = newC

print("Final means (K=3):\n", centroids)
