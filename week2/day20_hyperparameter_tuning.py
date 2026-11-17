
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

# Step 1: Create dataset
X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10],
    [11], [12], [13], [14], [15],
    [16], [17], [18], [19], [20]
])

y = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1
])

# Step 2: Create KNN model
model = KNeighborsClassifier()

# Step 3: Define hyperparameters
param_grid = {
    "n_neighbors": [1, 3, 5, 7]
}

# Step 4: Create GridSearchCV
grid_search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="accuracy"
)

# Step 5: Train and search
grid_search.fit(X, y)

# Step 6: Display best results
print("Best Parameters:", grid_search.best_params_)

print("Best Accuracy:", grid_search.best_score_)

print("Best Model:", grid_search.best_estimator_)
