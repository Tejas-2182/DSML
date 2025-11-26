import numpy as np, pandas as pd

pts = pd.read_csv("kmeans2_synthetic.csv").to_numpy()[:,1:].astype(float)  # drop id
m1, m2 = pts[0].copy(), pts[7].copy()

def assign(pts, cts):
    D = np.linalg.norm(pts[:,None,:]-cts[None,:,:], axis=2)
    return D.argmin(axis=1)

def update(pts, labels, k):
    return np.vstack([pts[labels==i].mean(axis=0) for i in range(k)])

for _ in range(10):
    labels = assign(pts, np.vstack([m1,m2]))
    newC = update(pts, labels, 2)
    if np.allclose(newC, np.vstack([m1,m2])): break
    m1, m2 = newC

# P6 index = 5
p6_cluster = labels[5] + 1
pop_c2 = (labels==1).sum()
print("Final m1:", m1, "m2:", m2)
print("1) P6 cluster:", p6_cluster)
print("2) Population around m2:", pop_c2)
print("3) Updated m1,m2 shown above.")
