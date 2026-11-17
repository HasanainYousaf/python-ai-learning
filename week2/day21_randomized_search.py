
import numpy as np

from sklearn.model_selection import RandomizedSearchCV
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

# Step 2: Create model
model = KNeighborsClassifier()

# Step 3: Define parameter options
param_grid = {
    "n_neighbors": [1, 3, 5, 7, 9, 11, 13]
}

# Step 4: Create RandomizedSearchCV
random_search = RandomizedSearchCV(
    model,
    param_grid,
    n_iter=4,
    cv=5,
    scoring="accuracy",
    random_state=42
)

# Step 5: Train and search
random_search.fit(X, y)

# Step 6: Display results
print("Best Parameters:", random_search.best_params_)

print("Best Accuracy:", random_search.best_score_)

print("Best Model:", random_search.best_estimator_)
