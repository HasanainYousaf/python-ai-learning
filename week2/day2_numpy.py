import numpy as np
#creating first numpy array
numbers=np.array([10,20,30,40])
print(numbers)
print(type(numbers))
#add 10 into every element 
print(numbers+10)

#Create an array of student marks:
marks=np.array([65,75,85,95])
#5 bonus to every student
print(marks+5)

#NumPy Array Creation Functions

# Q1: Create an array of 5 zeros.
zeros_array=np.array(5)
print(zeros_array)
# Q2 creating an array of 6 ones
ones_array=np.array(6)
print(ones_array)
# Q3: Create an array from 1 to 20
numbers=np.arange(1,21)
print(numbers)
# Q4: Create even numbers from 2 to 20
even_numbers=np.arange(2,21)
print(even_numbers)
# Q5: Create 5 evenly spaced numbers between 0 and 100
values=np.linspace(0,100,5)
print(values)

#numpy indexing and slicing practices 
import numpy as np
numbers=np.array([10,20,30,40,50,60])
# Q1: Print the first element
print(numbers[0])
# Q2: Print the last element.
print(numbers[5])
# Q3: Print the element at index 3.
print(numbers[3])
# Q4: Print elements from index 1 to 4.
print(numbers[1:4])
# Q5: Print the first three elements.
print(numbers[:3])
# Q6: Reverse the complete array.
print(numbers[::-1])

# Q7: Create a 2D array:
array=np.array([
 [10, 20, 30],
 [40, 50, 60],
 [70, 80, 90]])
# Q8: Print the number 50 from the 2D array.
print(array[1,1])
# Q9: Print the first row.
print(array[0])
print(array[ :,1])

#Mini Project: Student Marks Analyzer
marks=np.array([
    [50,60,70],
    [55,65,75],
    [80,90,95]
])
# Display first student's marks
print("first student marks:",marks[0])
# Display second subject marks of all students
print("second subject",marks[:,1])
# Display first student's first subject marks
print("First Mark:", marks[0, 0])

#numpy mathematical operation and aggregation

# Q1: Create an array [10, 20, 30, 40, 50]
numbers=np.array([10,20,30,40])
# Q2: Add 10 to every element
print(numbers+10)
# Q3: Subtract 5 from every element
print(numbers-5)
# Q4: Multiply every element by 3
print(numbers*3)
# Q5: Divide every element by 2
print(numbers/2)
# Q6: Calculate the sum of numbers
print(numbers.sum())
# Q7: Calculate the average
print(np.mean(numbers))
# Q8: Find the maximum value
print(np.max(numbers))
# Q9: Find the minimum value
print(np.min(numbers))
# Q10: Calculate standard deviation
print(np.std(numbers))

# Mini Project: Student Marks Analyzer

import numpy as np

marks = np.array([65, 75, 85, 95, 80])

print("Student Marks:", marks)
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))
print("Bonus Marks:", marks + 5)


# Day 2 Practice Solutions: Mathematical Operations

import numpy as np

# Q1: Create an array [10, 20, 30, 40, 50]
numbers = np.array([10, 20, 30, 40, 50])

# Q2: Add 10 to every element
print("Addition:", numbers + 10)

# Q3: Subtract 5 from every element
print("Subtraction:", numbers - 5)

# Q4: Multiply every element by 3
print("Multiplication:", numbers * 3)

# Q5: Divide every element by 2
print("Division:", numbers / 2)

# Q6: Calculate the sum
print("Sum:", np.sum(numbers))

# Q7: Calculate the average
print("Average:", np.mean(numbers))

# Q8: Find maximum value
print("Maximum:", np.max(numbers))

# Q9: Find minimum value
print("Minimum:", np.min(numbers))

# Q10: Calculate standard deviation
print("Standard Deviation:", np.std(numbers))
