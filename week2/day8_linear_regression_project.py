
# Week 2 - Day 8
# Mini Project: Student Marks Prediction

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 1: Create dataset
# X = Study hours
# y = Student marks

X = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]])

y = np.array([15, 20, 30, 35, 45,
              50, 60, 65, 75, 85])

# Step 2: Create the model
model = LinearRegression()

# Step 3: Train the model
model.fit(X, y)

# Step 4: Predict marks
predictions = model.predict(X)

# Step 5: Predict marks for a new student
study_hours = np.array([[7.5]])
predicted_marks = model.predict(study_hours)

print("Student Marks Prediction")
print("------------------------")
print("Study Hours:", study_hours[0][0])
print("Predicted Marks:", round(predicted_marks[0], 2))

# Step 6: Evaluate the model
mae = mean_absolute_error(y, predictions)
r2 = r2_score(y, predictions)

print("\nModel Evaluation")
print("MAE:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Step 7: Visualize results
plt.scatter(X, y, label="Actual Marks")
plt.plot(X, predictions, color="red", label="Regression Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Marks Prediction")
plt.legend()
plt.grid(True)
plt.show()
