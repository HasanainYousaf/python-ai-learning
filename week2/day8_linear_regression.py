
# Import Linear Regression
from sklearn.linear_model import LinearRegression

# Training data
# X = Study Hours
X = [[1], [2], [3], [4], [5]]

# y = Student Marks
y = [20, 30, 40, 50, 60]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Display slope and intercept
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict marks for 6 study hours
prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])

# Predict marks for 8 study hours
prediction2 = model.predict([[8]])

print("Predicted Marks for 8 Hours:", prediction2[0])

#Practices Questions
#Create training data:
#X = [[1], [2], [3], [4], [5]]
#y = [15, 25, 35, 45, 55]



#Train a Linear Regression model.

#Q2. Predict marks for 6 study hours.

#Q3. Display the slope and intercept.

#Q4. Predict marks for 10 study hours.

#Q5. Change the training data and observe how predictions change.

# Import Linear Regression
from sklearn.linear_model import LinearRegression

# Q1. Create training data
X = [[1], [2], [3], [4], [5]]
y = [15, 25, 35, 45, 55]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Q2. Predict marks for 6 study hours
prediction = model.predict([[6]])

print("Predicted Marks for 6 Hours:", prediction[0])

# Q3. Display slope and intercept
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Q4. Predict marks for 10 study hours
prediction2 = model.predict([[10]])

print("Predicted Marks for 10 Hours:", prediction2[0])

# Q5. Change training data
X_new = [[1], [2], [3], [4], [5]]
y_new = [20, 40, 60, 80, 100]

# Create and train new model
model_new = LinearRegression()
model_new.fit(X_new, y_new)

# Make new prediction
new_prediction = model_new.predict([[6]])

print("New Predicted Marks:", new_prediction[0])

