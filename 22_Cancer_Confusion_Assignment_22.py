TP, FN = 90, 210
FP, TN = 140, 9560
accuracy = (TP+TN)/(TP+TN+FP+FN)
error = 1-accuracy
precision = TP/(TP+FP)
recall = TP/(TP+FN)
print(f"Accuracy={accuracy:.6f}\nError={error:.6f}\nPrecision={precision:.6f}\nRecall={recall:.6f}")
