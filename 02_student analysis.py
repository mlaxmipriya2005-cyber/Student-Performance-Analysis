import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students.csv")

# Calculate average marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Top student
top_student = df.loc[df["Average"].idxmax()]
print("Top Student:\n", top_student)

# Subject-wise average
subject_avg = df[["Maths", "Science", "English"]].mean()
print("\nSubject-wise Average:\n", subject_avg)

# Bar chart
plt.figure()
subject_avg.plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.savefig("bar_chart_task2.png")

# Pie chart
plt.figure()
subject_avg.plot(kind="pie", autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.ylabel("")
plt.savefig("pie_chart_task2.png")

print("\nCharts saved successfully!")
