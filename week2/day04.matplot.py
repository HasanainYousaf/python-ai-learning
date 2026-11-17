import matplotlib.pyplot as plt
# Q1: Create a line plot for days [1,2,3,4,5]
# and marks [50,60,70,80,90].

# Q2: Add title "My Learning Progress".

# Q3: Add X-axis label "Days".

# Q4: Add Y-axis label "Marks".
days=[1,2,3,4,5]
marks=[50,60,70,80,90,]
plt.plot(days,marks)
plt.title("My learning progress")
plt.xlabel("Days")
plt.ylabel('Marks')
plt.show()

# Part 2 Practice

# Q5: Create a bar chart for 5 students and their marks.
students=['hasan','ali','mina','alia','ahmad']
marks=[50,60,84,76,59]
plt.bar(students,marks)
plt.title("students marks")
plt.xlabel('students')
plt.ylabel('marks')
plt.show()

# Q6: Create a scatter plot for study hours and marks.
hours=[1,2,3,4,7]
marks=[60,90,55,67,70]
plt.scatter(hours,marks)
plt.title("study hours")
plt.xlabel("hours")
plt.ylabel('marks')
plt.show()

# Q7: Create a histogram using 10 student marks.
marks=[60,55,64,72,60,83,95,79,81,79]
plt.hist(marks)
plt.title("marks distribution")
plt.xlabel("marks")
plt.ylabel("frequency")
plt.show()

# Part 3 Practice

# Q9: Create a pie chart for Python, Math, and AI marks.
subject=['python','math','Ai']
marks=[90,80,70]
plt.pie(marks, labels=subject, autopct='%1.1f%%')
plt.title("subject mark distribution")
plt.show()

# Q10: Display percentages in the pie chart.

# Q11: Create a line graph with grid enabled.
# Q12: Create a line graph with red color and circular markers.
# Q13: Add labels and legend to the graph.
days=[1,2,3,4,5]
marks=[50,60,70,80,90,]
plt.plot(days,marks,color='red',marker='o')
plt.title("line graph")
plt.xlabel("Days")
plt.ylabel('Marks')
plt.grid(True)
plt.show()


# Week 2 Day 4
# Mini Project: Student Performance Visualization

import matplotlib.pyplot as plt

# Student Data
students = ["Hasan", "Ali", "Ahmad", "Usman", "Bilal"]
marks = [85, 90, 75, 60, 95]

# Graph 1: Bar Chart
plt.figure()
plt.bar(students, marks)
plt.title("Final Exam Rsults")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Graph 2: Line Plot
plt.figure()
plt.plot(students, marks,color='red',marker="o")
plt.title("Student Marks Progress")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# Graph 3: Histogram
plt.figure()
plt.hist(marks, bins=3)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Graph 4: Pie Chart
plt.figure()
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Student Marks Distribution")
plt.show()




