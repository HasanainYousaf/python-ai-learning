
# Week 2 Day 3 - Pandas Practice

import pandas as pd

# Q1: Create a Series containing 5 numbers.
series=pd.Series([10,20,30,40,50])
print(series)

# Q2: Create a DataFrame with 3 students.
# Columns: Name, Marks, Age
Data={
    "Name":['hassaan','ali','azlan'],
    "marks" :[70,80,65],
    "Age":[20,19,21]
}  
# Q3: Print the DataFrame.
df= pd.DataFrame(Data) 
print(df)

# Q4: Create a Series containing marks:
# 60, 70, 80, 90, 100
df=pd.Series([60,70,80,90,100])
print(df)

# Week 2 Day 3 - Part 2 Practice

import pandas as pd

data = {
    "Name": ["Hasan", "Ali", "Ahmad", "Usman", "Bilal", "Hamza"],
    "Marks": [80, 90, 75, 85, 70, 95]
}

df = pd.DataFrame(data)
print(df)

# Q5: Display first 3 students.
print(df.head(3))

# Q6: Display last 2 students.
print(df.tail(2))

# Q7: Print number of rows and columns.
print(df.shape)

# Q8: Print all column names.
print(df.columns)

# Q9: Display statistical summary.
print(df.describe)

# Q10: Display the first 4 students.
print(df.head(4))

# Part 3: Selecting Columns and Rows

import pandas as pd

data = {
    "Name": ["Hasan", "Ali", "Ahmad", "Usman"],
    "Marks": [80, 90, 75, 85],
    "Age": [21, 22, 20, 23]
}

df = pd.DataFrame(data)


# Q11: Print only the Name column.
print(df['Name'])

# Q12: Print only the Marks column.
print(df['Marks'])

# Q13: Print Name and Age columns.
print(df[['Name','Age']])

# Q14: Print the first student using iloc.
print(df.iloc[0])

# Q15: Print the third student using iloc.
print(df.iloc[2])

# Q16: Print the first two students using iloc.
print(df.iloc[0:2])

# Q17: Print the row with index label 2 using loc.
print(df.loc[1])

import pandas as pd

data = {
    "Name": ["Hasan", "Ali", "Ahmad", "Usman", "Bilal"],
    "Marks": [80, 90, 75, 85, 60]
}

df = pd.DataFrame(data)
print(df)
# Part 4: Filtering Practice

# Q18: Display students whose marks are greater than 80.
print(df[df['Marks'] >80])

# Q19: Display students whose marks are less than 75.
print(df[df["Marks"]<75])

# Q20: Display students whose marks are equal to 90.
print(df[df["Marks"]==90])

# Q21: Display students whose marks are greater than or equal to 80.
print(df[df["Marks"]>=80])

# Q22: Display students whose marks are between 70 and 90.
print(df[(df["Marks"]>70)& (df["Marks"]<=90)])

# Q23: Display students whose marks are either 60 or 90.
print(df[(df["Marks"]==60)|(df["Marks"]==90)])


# Part 5: Reading CSV Files

import pandas as pd

df = pd.read_csv("week2/student.csv")

print(df)
# Q24: Read students.csv using pd.read_csv().

# Q25: Display first 3 students.
print(df.head(3))

# Q26: Calculate average marks.
print(df["Marks"].mean())

# Q27: Display students with marks greater than 80.
print(df["Marks"]>80)

# Q28: Save DataFrame into students_output.csv.
df.to_csv("week2/students_output.csv", index=False)



# Week 2 Day 3 - Pandas Mini Project
# Student Performance Analyzer

import pandas as pd

# Step 1: Create Student Data
data = {
    "Name": ["Hasan", "Ali", "Ahmad", "Usman", "Bilal"],
    "Python": [85, 90, 75, 60, 95],
    "Math": [80, 85, 70, 65, 90],
    "AI": [90, 95, 80, 70, 100]
}

df = pd.DataFrame(data)

# Step 2: Display Dataset
print("Student Dataset:")
print(df)

# Step 3: Calculate Average Marks
df["Average"] = df[["Python", "Math", "AI"]].mean(axis=1)

print("\nStudent Average Marks:")
print(df[["Name", "Average"]])

# Step 4: Highest Average
print("\nHighest Average:")
print(df["Average"].max())

# Step 5: Lowest Average
print("\nLowest Average:")
print(df["Average"].min())

# Step 6: Display Students with Average >= 80
print("\nStudents with Average >= 80:")
print(df[df["Average"] >= 80])

# Step 7: Save Dataset
df.to_csv("week2/student_results.csv", index=False)

print("\nDataset saved successfully!")

