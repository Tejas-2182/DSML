import numpy as np, pandas as pd

P = pd.read_csv("kmeans3_synthetic.csv").to_numpy()
pts = P[:,1:].astype(float)
m1, m2, m3 = pts[0].copy(), pts[3].copy(), pts[6].copy()

def assign3(pts, C):
    D = np.linalg.norm(pts[:,None,:]-C[None,:,:], axis=2)
    return D.argmin(axis=1)

def update(pts, labels, k):
    return np.vstack([pts[labels==i].mean(axis=0) for i in range(k)])

for _ in range(10):
    labels = assign3(pts, np.vstack([m1,m2,m3]))
    newC = update(pts, labels, 3)
    if np.allclose(newC, np.vstack([m1,m2,m3])): break
    m1, m2, m3 = newC

p6_cluster = labels[5] + 1
pop_c3 = (labels==2).sum()
print("Final m1:", m1, "m2:", m2, "m3:", m3)
print("1) P6 cluster:", p6_cluster)
print("2) Population around m3:", pop_c3)
print("3) Updated m1,m2,m3 shown above.")
