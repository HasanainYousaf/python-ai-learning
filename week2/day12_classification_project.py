#Mini Project Student pass/fail Prediction

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Create dataset
X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10],
    [11], [12], [13], [14], [15]
])

# 0 = Fail, 1 = Pass
y = np.array([
    0, 0, 0, 0, 0,
    0, 1, 1, 1, 1,
    1, 1, 1, 1, 1
])

# Step 2: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Create model
model = LogisticRegression()

# Step 4: Train model
model.fit(X_train, y_train)

# Step 5: Predict test results
y_pred = model.predict(X_test)

# Step 6: Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Step 7: Predict a new student's result
new_student = np.array([[5]])

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("\nStudent Result: Pass")
else:
    print("\nStudent Result: Fail")