import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

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

# Step 3: Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Step 4: Train model
model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate model
print("Actual Results:", y_test)
print("Predicted Results:", y_pred)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 7: Predict a new student
new_student = np.array([[8]])

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Student Result: Pass")
else:
    print("Student Result: Fail")