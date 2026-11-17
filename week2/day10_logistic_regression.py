
# Week 2 - Day 9
# Part 3: Logistic Regression

import numpy as np
from sklearn.linear_model import LogisticRegression

# Step 1: Create dataset
# X = Study hours
# y = 0 means Fail, 1 means Pass

X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

y = np.array([0, 0, 0, 0, 0,
              1, 1, 1, 1, 1])

# Step 2: Create Logistic Regression model
model = LogisticRegression()

# Step 3: Train the model
model.fit(X, y)

# Step 4: Predict for a new student
study_hours = np.array([[7]])

prediction = model.predict(study_hours)

# Step 5: Display prediction
if prediction[0] == 1:
    print("Student Result: Pass")
else:
    print("Student Result: Fail")

# Step 6: Display probability
probability = model.predict_proba(study_hours)

print("Fail Probability:", round(probability[0][0] * 100, 2), "%")
print("Pass Probability:", round(probability[0][1] * 100, 2), "%")
