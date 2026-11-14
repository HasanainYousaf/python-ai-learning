
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# =====================================
# 1. CREATE DATASET
# =====================================

data = {
    "Name": ["Ali", "Ahmed", "Hasan", "Sara", "Ayesha", "Usman"],
    "Age": [20, 21, None, 22, 20, 23],
    "Gender": ["Male", "Male", "Male", "Female", "Female", "Male"],
    "Hours_Studied": [2, 4, 5, 6, 8, 10],
    "Marks": [35, 50, 60, None, 85, 95]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# =====================================
# 2. HANDLE MISSING VALUES
# =====================================

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# =====================================
# 3. ENCODING
# =====================================

# One-Hot Encoding Gender
df = pd.get_dummies(df, columns=["Gender"], dtype=int)

# =====================================
# 4. FEATURE SCALING
# =====================================

scaler = MinMaxScaler()

df[["Age", "Hours_Studied"]] = scaler.fit_transform(
    df[["Age", "Hours_Studied"]]
)

# =====================================
# 5. PREPARE FEATURES AND TARGET
# =====================================

X = df.drop(columns=["Name", "Marks"])
y = df["Marks"]

# =====================================
# 6. TRAIN-TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================
# 7. DISPLAY RESULTS
# =====================================

print("\nPreprocessed Dataset:")
print(df)

print("\nTraining Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)

print("\nTraining Size:", len(X_train))
print("Testing Size:", len(X_test))



#Understand Project Workflow
#Original Dataset

#Missing Values Handling

#Categorical Encoding

#Feature Scaling

#Train-Test Split

#Ready for Machine Learning
