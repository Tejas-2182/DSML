TP, FP, FN, TN = 1, 1, 8, 90
accuracy = (TP+TN)/(TP+TN+FP+FN)
error = 1-accuracy
precision = TP/(TP+FP) if TP+FP else 0
recall = TP/(TP+FN) if TP+FN else 0
print(f"Accuracy={accuracy:.4f}, Error={error:.4f}, Precision={precision:.4f}, Recall={recall:.4f}")
