# Task 1 (Easy):
# Create a pie chart of car brands:
# Values: [40, 30, 20, 10]
# Labels: ['Maruti Suzuk', 'Audi', 'Porsche', 'Honda']
#  Add title and legend.
import matplotlib.pyplot as plt

values = [40, 30, 20, 10]
labels = ['Maruti Suzuki', 'Audi', 'Porsche', 'Honda']

plt.figure()
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Car Brand Distribution")
plt.legend(labels)
plt.show()


# Task 2:
# Same data as above
#  Add explode for the biggest slice.
import matplotlib.pyplot as plt

values = [40, 30, 20, 10]
labels = ['Maruti Suzuki', 'Audi', 'Porsche', 'Honda']

explode = [0.1, 0, 0, 0]

plt.figure()
plt.pie(values, labels=labels, explode=explode, autopct='%1.1f%%')
plt.title("Car Brand Distribution with Explode")
plt.legend(labels)
plt.show()


# Create a pie chart of:
# • Tea = 55
# • Coffee = 30
# • Juice = 15
#  Show percentage with '%1.1f%%'
import matplotlib.pyplot as plt

values = [55, 30, 15]
labels = ['Tea', 'Coffee', 'Juice']

plt.figure()
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Beverage Prefrence")
plt.legend(labels)
plt.show()


# Task 4 (Medium):
# Create a donut chart (pie chart with a hole in the center).
import matplotlib.pyplot as plt

values = [55, 30, 15]
labels = ['Tea', 'Coffee', 'Juice']

plt.figure()

wedges, texts, autotexts = plt.pie(values, labels=labels, autopct='%1.1f%%')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Beverage Preference - Donut Chart")
plt.legend(labels)
plt.show()


# Task 5:
# Create a pie chart where:
# • You set your own 5 colors
# • Randomly pick one slice to explode
# • Add shadow
# • Use startangle=180
import matplotlib.pyplot as plt
import random

values = [25, 20, 15, 30, 10]
labels = ['A', 'B', 'C', 'D', 'E']

colors = ['red', 'green', 'blue', 'orange', 'purple']

explode_index = random.randint(0, len(values) - 1)  
explode = [0.1 if i == explode_index else 0 for i in range(len(values))]

plt.figure()

plt.pie(values,
        labels=labels,
        colors=colors,
        explode=explode,
        shadow=True,
        startangle=180,
        autopct='%1.1f%%')

plt.title("Task 5 - customized Pie Chart")
plt.legend(labels)
plt.show()


# Task 6 (Hard):
# Take 7 categories (your choice),
# Sort them in descending order (largest to smallest),
# THEN plot the pie chart.
import matplotlib.pyplot as plt

values = [50, 10, 30, 20, 40, 5, 25]
labels = ['Cat A', 'Cat B', 'Cat C', 'Cat D', 'Cat E', 'Cat F', 'Cat G']

sorted_pairs = sorted(zip(values, labels), reverse=True)
sorted_values, sorted_labels = zip(*sorted_pairs)

plt.figure()
plt.pie(sorted_values, labels=sorted_labels, autopct='%1.1f%%')
plt.title("Task 6 - Sorted Pie Chart (Descending Order)")
plt.legend(sorted_labels)
plt.show()


# AREA CHART (fill_between) TASKS
# Task 7 (Easy):
# Plot x = [1,2,3,4,5,6]
# y = [5,3,6,7,2,8]
#  Use fill_between with 0.4 alpha.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [5, 3, 6, 7, 2, 8]

plt.figure()
plt.fill_between(x, y, alpha=0.4)
plt.title("Task 7 -  Area Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()


# Task 8:
# Same data
#  Fill area between y and another line:
# y2 = [2,2,2,2,2,2]
# Use:
# plt.fill_between(x, y, y2)
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [5, 3, 6, 7, 2, 8]
y2 = [2, 2, 2, 2, 2, 2]  

plt.figure()

plt.fill_between(x, y, y2, alpha=0.4)

plt.plot(x, y, label="y")
plt.plot(x, y2, label="y2")

plt.title("Task 8 - Area Between Two Lines")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.show()


# Task 9:
# Create an area chart of:
# Temperature (°C): [20,22,25,27,30,29]
# Hours: [1,2,3,4,5,6]
#  Add labels, grid, title.
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
temperature = [20, 22, 25, 27, 30, 29]

plt.figure()
plt.fill_between(hours, temperature, alpha=0.4)  
plt.plot(hours, temperature) 

plt.title("Task 9 - Temperature Throughout the Day")
plt.xlabel("Hours")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()


# Task 10 (Medium):
# Create an area chart with two lines:
# line1 = [3,4,5,6,7]
# line2 = [2,3,3,4,6]
#  Plot both using two different fill colors
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
line1 = [3, 4, 5, 6, 7]
line2 = [2, 3, 3, 4, 6]

plt.figure()

plt.fill_between(x, line1, alpha=0.4, label="Line 1")
plt.plot(x, line1)

plt.fill_between(x, line2, alpha=0.4, label="Line 2")
plt.plot(x, line2)

plt.title("Task 10 - Two Line Area Chart")
plt.xlabel("X values")
plt.ylabel("Values")
plt.legend()
plt.grid(True)

plt.show()


# Task 11 (Hard):
# Generate random data using NumPy for 50 points:
# x = np.arange(50)
# y = np.random.randint(1,100,50)
#  Plot an area chart with alpha=0.3.
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.arange(50)  
    y = np.random.randint(1, 100, 50) 

    plt.figure()

    plt.fill_between(x, y, alpha=0.3) 
    plt.plot(x, y) 

    plt.title("Task 11 - Random Data Area Chart")
    plt.xlabel("Index")
    plt.ylabel("Random Values")
    plt.grid(True)

    plt.show()



# Task 12 (Easy):
# Given:
# days = [1,2,3,4,5]
# sales_A = [10,20,30,40,50]
# sales_B = [5,10,15,20,25]
# sales_C = [3,6,9,12,15]
#  Create a stacked area chart.
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales_A = [10, 20, 30, 40, 50]
sales_B = [5, 10, 15, 20, 25]
sales_C = [3, 6, 9, 12, 15]

plt.figure()

plt.stackplot(days, sales_A, sales_B, sales_C, labels=['Sales A', 'Sales B', 'Sales C'], alpha=0.6)

plt.title("Task 12 - Stacked Area Chart")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.show()


# Task 13:
# Add:
# • Edgecolor='black'
# • Alpha = 0.7
# • Proper legend
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales_A = [10, 20, 30, 40, 50]
sales_B = [5, 10, 15, 20, 25]
sales_C = [3, 6, 9, 12, 15]

plt.figure()

plt.stackplot(days, sales_A, sales_B, sales_C,
              labels=['Sales A', 'Sales B', 'Sales C'],
              alpha=0.7, edgecolor='black')

plt.title("Task 13 - Stacked Area Chart with Edge Colors")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend(loc="upper left")
plt.grid(True)

plt.show()


# Task 14 (Medium):
# Create a stacked area chart of 4 products with 7 days of data.
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
product_A = [5, 10, 15, 20, 25, 30, 35]
product_B = [3, 6, 9, 12, 15, 18, 21]
product_C = [4, 8, 12, 16, 20, 24, 28]
product_D = [2, 4, 6, 10, 12, 14, 16]

plt.figure()

plt.stackplot(days, product_A, product_B, product_C, product_D,
              labels=['Product A', 'Product B', 'Product C', 'Product D'],
              alpha=0.7, edgecolor='black')

plt.title("Task 14 - Stacked Area Chart of 4 Products (7 Days)")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend(loc="upper left")
plt.grid(True)

plt.show()


# Task 15:
# Use random data for 100 days (4 products) using NumPy.
# Plot a stacked area chart with:
# • 4 layers
# • Proper title, labels
# • Thin black border (edgecolor='black')
import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 101)  
product_A = np.random.randint(20, 80, 100)
product_B = np.random.randint(10, 60, 100)
product_C = np.random.randint(5, 40, 100)
product_D = np.random.randint(1, 30, 100)

plt.figure(figsize=(12, 6))

plt.stackplot(days, product_A, product_B, product_C, product_D,
              labels=['Product A', 'Product B', 'Product C', 'Product D'],
              edgecolor='black', linewidth=0.5, alpha=0.7)

plt.title("Task 15 - Stacked Area Chart (100 Days, Random Data)")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend(loc="upper left")
plt.grid(True)

plt.show()


# Task 16 (Hard): REAL DATA TASK
# Imagine monthly revenue data (12 months):
# • Food delivery
# • Clothing
# • Electronics
# • Rent
#  Generate realistic data yourself
#  Plot a stacked area chart
#  Add grid + legend + labels
import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
food_delivery = np.random.randint(200, 500, 12)
clothing = np.random.randint(150, 400, 12)
electronics = np.random.randint(250, 600, 12)
rent = np.random.randint(300, 700, 12)

plt.figure(figsize=(12, 6))

plt.stackplot(months, food_delivery, clothing, electronics, rent,
              labels=['Food Delivery', 'Clothing', 'Electronics', 'Rent'],
              alpha=0.7, edgecolor='black')

plt.title("Task 16 - Monthly Revenue (Stacked Area Chart)")
plt.xlabel("Month")
plt.ylabel("Revenue (in $1000s)")
plt.legend(loc="upper left")
plt.grid(True)

plt.show()
