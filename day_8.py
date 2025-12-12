# Task 1 — 
# Draw a Scatter Plot with Different Shapes
# Create a scatter plot for:
# x = [5,10,15,20,25]
# y = [10,30,20,40,60]
# Conditions:
# • Each point must have different color
# • Each point must have different size
# • Add grid, title, labels
# • Add a dotted line (--) joining the points
import matplotlib.pyplot as plt


x = [5, 10, 15, 20, 25]
y = [10, 30, 20, 40, 60]

colors = ['red', 'orange', 'blue', 'green', 'purple']
sizes = [50, 100, 150, 200, 250]

plt.scatter(x, y, c=colors, s=sizes)

plt.plot(x, y, linestyle='--')

plt.title("Scatter Plot With Different Colors & Sizes")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

plt.show()


# Task 2 
# — Two Groups, Two Scatter Plots
# Make 2 groups:
# Group A
# x = [1,3,5,7]
# y = [10,18,12,25]
# Group B
# x = [2,4,6,8]
# y = [22,28,30,35]
# Conditions:
# • Plot both groups using scatter
# • Give different colors
# • Add legend
# • Add title: "Performance Comparison"
# • Add x label: "Time"
# • Add y label: "Score"
import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7]
y1 = [10, 18, 12, 25]

x2 = [2, 4, 6, 8]
x2 = [22, 28, 30, 35]

plt.scatter(x1, y1, color='blue', label='Group A')
plt.scatter(x2, y2, colors='red', label='Group B')

plt.title("Performance Comparison")
plt.xlabel("Time")
plt.ylabel("Score")

plt.legend()

plt.show()


# Task 3 — Horizontal Bar Chart
# Categories:
# ['Apple','Banana','Mango','Orange']
# Values:
# [50, 80, 40, 90]
# Conditions:
# • Use different colors
# • Show value on each bar using plt.text()
# • Add title: "Fruit Sales Report"
import matplotlib.pyplot as plt

categories = ['Apple', 'Banana', 'Mango', 'Orange']
values = [50, 80, 40, 90]

colors = ['red', 'yellow', 'orange', 'green']

plt.barh(categories, values, color=colors)

for index, value in enumerate(values):
    plt.text(value + 1, index, str(value))

plt.title("Fruit Sales Report")
plt.xlabel("Sales")
plt.ylabel("Fruits")

plt.show()

Task 4 — Histogram of Student Marks
Create 100 random student marks between 1–100:
marks = np.random.randint(1,100,size=100)
Conditions:
• Show histogram with 10 bins
• Color = blue
• Edge color = black
• Add title: "Marks Distribution"

import numpy as np
import matplotlib.pyplot as plt

marks = np.random.randint(1, 100, size=100)

plt.hist(marks, bins=10, color='blue', edgecolor='black')

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

# Task 5 — Mixed Chart (Line + Scatter)
# Data:
# x = [1,2,3,4,5]
# y = [5,12,18,25,40]
# Conditions:
# • Draw line plot
# • Draw scatter plot on same graph
# • Line color = green
# • Scatter color = red
# • Add title, labels, grid

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 12, 18, 25, 40]

plt.plot(x, y, color='green', label='Line Plot')

plt.scatter(x, y, color='red', label='Data Points')

plt.title("Mixed Chart: Line + Scatter")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

plt.legend()

plt.show()


# Task 6 — Compare 3 Bar Charts in One Graph
# Categories:
# ['Math','Science','English']
# Scores:
# student1 = [80,60,75]
# student2 = [85,70,90]
# student3 = [78,68,82]
# Conditions:
# • Use bar chart for 3 students in same graph
# • Different colors
# • Add legend
# • Add title: "Student Performance Comparison"
import matplotlib.pyplot as plt
import numpy as np

categories = ['Math', 'Science', 'English']
student1 = [80, 60, 75]
student2 = [85, 70, 90]
student3 = [78, 68, 82]

x = np.arange(len(categories))
width = 0.25 

plt.bar(x - width, student1, width, color='red', label='Student 1')
plt.bar(x, student2, width, color='blue', label='Student 2')
plt.bar(x + width, student3, width, color='green', label='Student 3')

plt.title("Student Performance Comparison")
plt.xlabel("Subjects")
plt.ylabel("Scores")

plt.xticks(x, categories)

plt.legend()

plt.show()


# Task 7 — Multiple Histograms
# Create 2 datasets:
# d1 = np.random.randint(1,100,50)
# d2 = np.random.randint(1,100,50)
# Conditions:
# • Plot both histograms on same graph
# • Make them slightly transparent using alpha
# • Give different colors
# • Add legend
# • Add title
import numpy as np
import matplotlib.pyplot as plt

d1 = np.random.randint(1, 100, 50)
d2 = np.random.randint(1, 100, 50)

plt.hist(d1, bins=10, alpha=0.6, color='blue', label='Dataset 1')
plt.hist(d2, bins=10, alpha=0.6, color='red', label='Dataset 2')

plt.title("Multiple Histogram Comparison")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.legend()

plt.show()
