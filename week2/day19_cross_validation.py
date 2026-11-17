
import numpy as np

from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

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
model = LogisticRegression()

# Step 3: Create K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Step 4: Perform Cross-Validation
scores = cross_val_score(
    model, X, y, cv=kf, scoring="accuracy"
)

# Step 5: Display results
print("Cross Validation Scores:", scores)

print("Average Accuracy:", scores.mean())
