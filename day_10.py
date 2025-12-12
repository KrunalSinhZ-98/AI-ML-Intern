# PART 1: BOX PLOT TASKS
# Task 1:
# Create a box plot using a new list:
# data = [5, 15, 20, 22, 35, 60, 80]
import matplotlib.pyplot as plt

data = [5, 15, 20, 22, 35, 60, 80]

plt.boxplot(data)

plt.title("Box Plot - Task 1")
plt.ylabel("Values")

plt.show()


# Task 2:
# Change the box plot title to:
# ➡ "My First Custom Box Plot"
import matplotlib.pyplot as plt

data = [5, 15, 20, 22, 35, 60, 80]

plt.boxplot(data)
plt.title("My First Custom Box Plot")
plt.ylabel("Values")
plt.show()


# Task 3:
# Add an x-axis label to the box plot:
# ➡ "Sample Data"
import matplotlib.pyplot as plt

data = [5, 15, 20, 22, 35, 60, 80]

plt.boxplot(data)
plt.title("My First Custom Box Plot")
plt.xlabel("Sample Data")
plt.ylabel("Values")
plt.show()


# Task 4:
# Remove the grid from the box plot.
# (Hint: Don’t use plt.grid())
import matplotlib.pyplot as plt

data = [5, 15, 20, 22, 35, 60, 80]

plt.boxplot(data)
plt.title("My First Custom Box Plot")
plt.xlabel("Simple Data")
plt.ylabel("Values")

plt.show()


# Task 5:
# Create a box plot for 4 subjects instead of 3:
# Math, Science, English, Hindi
# hindi = [70, 72, 75, 80, 85, 90]
import matplotlib.pyplot as plt

math = [80, 85, 78, 92, 88, 75]
science = [70, 65, 72, 78, 82, 77]
english = [60, 62, 68, 70, 72, 74]
hindi = [70, 72, 75, 80, 85, 90]

data = [math, science, english, hindi]

plt.boxplot(data)
plt.title("Box Plot of Four Subjects")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.xticks([1, 2, 3, 4], ["Math", "Science", "English", "Hindi"])

plt.show()


# Task 6:
# Change the color of the box plot using:
# patch_artist=True
# boxprops=dict(facecolor='lightblue')
import matplotlib.pyplot as plt

math = [80, 85, 78, 92, 88, 75]
science = [70, 65, 72, 78, 82, 77]
english = [60, 62, 68, 70, 72, 74]
hindi = [70, 72, 75, 80, 85, 90]

data = [math, science, english, hindi]

plt.boxplot(data, patch_artist=True,
            boxprops=dict(facecolor='lightblue'))

plt.title("Colored Box Plot of Four Subjects")
plt.ylabel("Subjects")
plt.ylabel("Scores")
plt.xticks([1, 2, 3, 4], ["Math", "Science", "English", "Hindi"])

plt.show()


# Task 7:
# Create a title for subject marks box plot:
# ➡ "Student Subject Marks Distribution"
import matplotlib.pyplot as plt

math = [80, 85, 78, 92, 88, 75]
science = [70, 65, 72, 78, 82, 77]
english = [60, 62, 68, 70, 72, 74]
hindi = [70, 72, 75, 80, 85, 90]

data = [math, science, english, hindi]

plt.boxplot(data, patch_artist=True,
            boxprops=dict(facecolor='lightblue'))

plt.title("Student Subject Marks Distribution")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.xticks([1, 2, 3, 4], ["Math", "Science", "English", "Hindi"])

plt.show()


# Task 8:
# Create a word cloud using your own text:
# ➡ “I love Python. Python is awesome. Learning data science is fun.”
# from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "I love Python. Python is awesome. Learning data science is fun."

wordcloud = WordCloud(width=800, height=400).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud - Task 8")
plt.show()


# Task 9:
# Change the background color of the word cloud to:
# ➡ yellow
# from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "I love Python. Python is awesome. Learning data science is fun."

wordcloud = WordCloud(width=800, height=400, background_color="yellow").generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud - Yellow Background")
plt.show()


# Task 10:
# Generate 3 word clouds using different colormaps:
# • cool
# • plasma
# • spring
# from wordcloud import WordCloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Your sample text goes here for the word cloud generation example..."

wc_cool = WordCloud(width=1000, height=600, colormap='cool', background_color='white').generate(text)
wc_plasma = WordCloud(width=1000, height=600, colormap='plasma', background_color='white').generate(text)
wc_spring = WordCloud(width=1000, height=600, colormap='spring', background_color='white').generate(text)

plt.figure(figsize=(18, 10))

plt.subplot(1, 3, 1)
plt.imshow(wc_cool, interpolation='bilinear')
plt.title("Cool Colormap")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(wc_plasma, interpolation='bilinear')
plt.title("Plasma Colormap")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(wc_spring, interpolation='bilinear')
plt.title("Spring Colormap")
plt.axis('off')

plt.show()


# Task 11:
# Limit the word cloud to max_words = 20.
# from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "I love Python. Python is awesome. Learning data science is fun and exciting. Python helps build amazing things."

wordcloud = WordCloud(width=800, height=400, background_color="white", max_words=20).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud - Max 20 Words (Task 11)")
plt.show()


# Task 12:
# Read text from a new file:
# ➡ new_para.txt
# (Create the file yourself
# from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(width=900, height=450, background_color="white").generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud from new_para.txt - Task 12")
plt.show()


# Task 13:
# Change the word cloud size to:
# ➡ width = 1000, height = 600
# from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Your text goes here..."

wordcloud = WordCloud(width=1000, height=600, background_color='white').generate(text)

plt.figure(figsize=(12, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# Task 14:
# Save your word cloud image using:
# wc.to_file("my_wordcloud.png")
# from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = """Python is a powerful programming language. 
It is widely used in data science, machine learning, web development, 
and automation. Learning Python opens doors to many opportunities 
in the tech world. Python is fun to learn and easy to use."""

wc = WordCloud(width=1000, height=600, background_color="white").generate(text)

wc.to_file("my_wordcloud.png")

plt.figure(figsize=(14, 7))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud Saved as Image - Task 14")
plt.show()
