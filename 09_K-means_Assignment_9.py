import pandas as pd
import numpy as np

# Load points (ignoring the ID column)
data = pd.read_csv("kmeans2_synthetic.csv")
pts = data[["x", "y"]].values

# Initial centroids as given: m1 = P1, m2 = P8
m1 = pts[0].copy()
m2 = pts[7].copy()

# Function to assign each point to nearest centroid
def assign_cluster(points, c1, c2):
    labels = []
    for p in points:
        d1 = np.linalg.norm(p - c1)
        d2 = np.linalg.norm(p - c2)
        labels.append(0 if d1 <= d2 else 1)
    return np.array(labels)

# Function to update centroid
def update_centroid(points, labels, cluster_id):
    return points[labels == cluster_id].mean(axis=0)

# Run for 10 iterations or until convergence
for _ in range(10):
    labels = assign_cluster(pts, m1, m2)
    new_m1 = update_centroid(pts, labels, 0)
    new_m2 = update_centroid(pts, labels, 1)

    if np.allclose([new_m1, new_m2], [m1, m2]):
        break

    m1, m2 = new_m1, new_m2

# Questions
p6_cluster = labels[5] + 1           # +1 because clusters = 1 or 2
population_m2 = sum(labels == 1)

# Output
print("Final m1:", m1)
print("Final m2:", m2)
print("1) Cluster of P6:", p6_cluster)
print("2) Population of cluster around m2:", population_m2)
print("3) Updated centroids shown above.")
