
# Week 2 - Day 11
# Part 5: Confusion Matrix

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Step 1: Actual values
# 1 = Pass, 0 = Fail

y_actual = [1, 1, 1, 1, 1,
            0, 0, 0, 0, 0]

# Step 2: Predicted values

y_predicted = [1, 1, 1, 0, 0,
               1, 0, 0, 0, 0]

# Step 3: Confusion Matrix
cm = confusion_matrix(y_actual, y_predicted)

print("Confusion Matrix:")
print(cm)

# Step 4: Accuracy
accuracy = accuracy_score(y_actual, y_predicted)

print("\nAccuracy:", accuracy)

# Step 5: Precision
precision = precision_score(y_actual, y_predicted)

print("Precision:", precision)

# Step 6: Recall
recall = recall_score(y_actual, y_predicted)

print("Recall:", recall)

# Step 7: F1 Score
f1 = f1_score(y_actual, y_predicted)

print("F1 Score:", f1)
