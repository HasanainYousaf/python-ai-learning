
# Import evaluation metrics
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Actual values
actual = [80, 70, 90, 60]

# Predicted values
predicted = [75, 65, 85, 55]

# Calculate MAE
mae = mean_absolute_error(actual, predicted)

# Calculate MSE
mse = mean_squared_error(actual, predicted)

# Calculate R2 Score
r2 = r2_score(actual, predicted)

# Display results
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)
