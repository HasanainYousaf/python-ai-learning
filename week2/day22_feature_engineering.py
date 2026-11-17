
import pandas as pd

# Step 1: Create dataset
data = {
    "study_hours": [2, 4, 6, 8, 10],
    "attendance": [50, 60, 70, 80, 90],
    "marks": [30, 45, 60, 75, 90]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Create new feature
df["study_effort"] = (
    df["study_hours"] * df["attendance"] / 100
)

# Step 3: Create another feature
df["performance"] = df["marks"] / 100

# Step 4: Display updated dataset
print("\nUpdated Dataset:")
print(df)
