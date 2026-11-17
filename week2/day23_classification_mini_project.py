
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Step 1: Create dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 6, 7, 8, 9, 10, 5, 6],

    "attendance": [40, 45, 50, 55, 60, 65, 70, 75, 80, 90,
                   42, 48, 53, 67, 72, 78, 85, 95, 62, 69],

    "previous_marks": [20, 25, 30, 35, 40, 45, 50, 55, 60, 90,
                       22, 28, 33, 47, 52, 58, 65, 95, 42, 48],

    "result": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
               0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Step 2: Select features and target
X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]

# Step 3: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Scale features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Create model
model = RandomForestClassifier(random_state=42)

# Step 6: Train model
model.fit(X_train_scaled, y_train)

# Step 7: Make predictions
y_pred = model.predict(X_test_scaled)

# Step 8: Evaluate model
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Step 9: Predict a new student
new_student = pd.DataFrame({
    "study_hours": [8],
    "attendance": [85],
    "previous_marks": [75]
})

new_student_scaled = scaler.transform(new_student)

prediction = model.predict(new_student_scaled)

if prediction[0] == 1:
    print("\nStudent Result: PASS")
else:
    print("\nStudent Result: FAIL")
