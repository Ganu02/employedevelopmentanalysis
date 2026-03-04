import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Create Dataset
# -----------------------------

data = {
    "name": ["Ganesh", "Amit", "Rahul", "Priya", "Sneha", "Kiran", "Rohit", "Pooja"],
    "age": [25, 30, 35, 40, 29, 45, 32, 38],
    "city": ["Mumbai", "Pune", "Mumbai", "Delhi", "Pune", "Delhi", "Mumbai", "Pune"],
    "salary": [25000, 30000, 40000, 50000, 28000, 60000, 35000, 45000],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data) 

print("===== DATASET =====")
print(df)


# -----------------------------
# STEP 2: Basic EDA
# -----------------------------

print("\n===== BASIC INFO =====")
print(df.info())

print("\n===== STATISTICS =====")
print(df.describe())


# -----------------------------
# STEP 3: GROUPING ANALYSIS
# -----------------------------

# Average salary by department
avg_salary_dept = df.groupby("department")["salary"].mean()
print("\nAverage Salary by Department:")
print(avg_salary_dept)

# Average salary by city
avg_salary_city = df.groupby("city")["salary"].mean()
print("\nAverage Salary by City:")
print(avg_salary_city)


# -----------------------------
# STEP 4: GRAPHS
# -----------------------------

# 1️⃣ Bar Chart - Average Salary by Department
plt.figure()
avg_salary_dept.plot(kind='bar')
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()


# 2️⃣ Bar Chart - Average Salary by City
plt.figure()
avg_salary_city.plot(kind='bar')
plt.title("Average Salary by City")
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.show()


# 3️⃣ Histogram - Salary Distribution
plt.figure()
plt.hist(df["salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()


# 4️⃣ Scatter Plot - Age vs Salary
plt.figure()
plt.scatter(df["age"], df["salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()