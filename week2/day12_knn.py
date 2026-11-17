import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Create dataset
X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

# 0 = Fail, 1 = Pass
y = np.array([
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1
])

# Step 2: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Step 4: Train model
model.fit(X_train, y_train)

# Step 5: Predict test results
y_pred = model.predict(X_test)

# Step 6: Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Actual Results:", y_test)
print("Predicted Results:", y_pred)
print("Accuracy:", accuracy)

# Step 7: Predict new student result
new_student = np.array([[7]])

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Student Result: Pass")
else:
    print("Student Result: Fail")