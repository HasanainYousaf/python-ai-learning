
# Import libraries
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Training data
X = [[1], [2], [3], [4], [5]]
y = [20, 30, 40, 50, 60]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Predict values
predicted = model.predict(X)

# Create scatter plot
plt.scatter(X, y, label="Actual Data")

# Draw regression line
plt.plot(X, predicted, label="Regression Line")

# Add labels and title
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression")

# Display legend
plt.legend()

# Show graph
plt.show()
