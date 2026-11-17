
import pandas as pd

from sklearn.feature_selection import SelectKBest, f_classif

# Step 1: Create dataset
data = {
    "study_hours": [2, 4, 6, 8, 10, 3, 5, 7, 9, 1],
    "attendance": [40, 50, 60, 80, 90, 45, 65, 75, 85, 30],
    "previous_marks": [20, 30, 50, 70, 90, 25, 45, 65, 85, 10],
    "student_id": [101, 102, 103, 104, 105,
                   106, 107, 108, 109, 110]
}

df = pd.DataFrame(data)

# Target column
y = [0, 0, 0, 1, 1, 0, 0, 1, 1, 0]

# Step 2: Select input features
X = df

# Step 3: Create feature selector
selector = SelectKBest(score_func=f_classif, k=2)

# Step 4: Select best features
X_selected = selector.fit_transform(X, y)

# Step 5: Display selected features
selected_features = X.columns[selector.get_support()]

print("Selected Features:")
print(selected_features.tolist())

print("\nSelected Data:")
print(X_selected)
