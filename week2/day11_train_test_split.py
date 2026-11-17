import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Input data: Study hours
X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

# Output: 0 = Fail, 1 = Pass
y = np.array([
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1
])

# Divide data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Training Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

print("\nActual Results:")
print(y_test)

print("\nPredicted Results:")
print(y_pred)

print("\nModel Accuracy:", accuracy)