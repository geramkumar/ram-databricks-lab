
# matplotlib_seaborn_basics_to_intermediate.py
# Author: OpenAI ChatGPT
# Purpose: Learn basic to intermediate data visualization using matplotlib and seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
np.random.seed(42)
data = {
    'age': np.random.randint(20, 60, size=100),
    'salary': np.random.normal(50000, 15000, 100).astype(int),
    'department': np.random.choice(['HR', 'IT', 'Finance', 'Marketing'], 100),
    'experience': np.random.randint(1, 20, 100),
    'gender': np.random.choice(['Male', 'Female'], 100)
}

df = pd.DataFrame(data)

# -------------------------------
# Matplotlib Basics
# -------------------------------

# 1. Line Plot
plt.figure(figsize=(8, 4))
plt.plot(df['age'], df['salary'], color='blue')
plt.title("Salary vs Age")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.savefig("line_plot.png")

# 2. Bar Plot
dept_counts = df['department'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(dept_counts.index, dept_counts.values, color='skyblue')
plt.title("Employees per Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("bar_plot.png")

# 3. Histogram
plt.figure(figsize=(6, 4))
plt.hist(df['salary'], bins=20, color='green', edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")

# 4. Pie Chart
gender_counts = df['gender'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("pie_chart.png")

# -------------------------------
# Seaborn Basics and Intermediate
# -------------------------------

# 5. Count Plot
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='department', palette='Set2')
plt.title("Department Distribution")
plt.tight_layout()
plt.savefig("sns_countplot.png")

# 6. Box Plot
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='department', y='salary', palette='Set3')
plt.title("Salary by Department")
plt.tight_layout()
plt.savefig("sns_boxplot.png")

# 7. Violin Plot
plt.figure(figsize=(6, 4))
sns.violinplot(data=df, x='gender', y='salary', palette='Set1')
plt.title("Salary Distribution by Gender")
plt.tight_layout()
plt.savefig("sns_violinplot.png")

# 8. Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='age', y='salary', hue='department', style='gender')
plt.title("Salary vs Age with Hue")
plt.tight_layout()
plt.savefig("sns_scatterplot.png")

# 9. Pair Plot
sns.pairplot(df[['age', 'salary', 'experience']], diag_kind='kde')
plt.suptitle("Pairwise Relationships", y=1.02)
plt.tight_layout()
plt.savefig("sns_pairplot.png")

# 10. Heatmap
pivot = pd.pivot_table(df, values='salary', index='department', columns='gender', aggfunc='mean')
plt.figure(figsize=(6, 4))
sns.heatmap(pivot, annot=True, cmap='coolwarm')
plt.title("Avg Salary Heatmap by Department and Gender")
plt.tight_layout()
plt.savefig("sns_heatmap.png")

print("All Matplotlib and Seaborn plots generated successfully.")
