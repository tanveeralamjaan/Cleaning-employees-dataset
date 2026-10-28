# import libraries
import numpy as np
import pandas as pd


# loading dataset
df = pd.read_csv("Cleaning-employees-dataset\indian_employee_data.csv")

# print(df.head(4))
# print("Missing valus in each column: ")
# print(df.isnull().sum())

# checking the missing values
# print(df.info())

# checking and replacing inf or -inf values with Nan values
print(np.isinf(df.select_dtypes(include="number")).sum())
df.replace([np.inf, -np.inf], np.nan, inplace = True)

# Replacing the missing values in salary with average salary
df["Salary_INR"] = df["Salary_INR"].fillna(df["Salary_INR"].mean(), inplace=True)

# Replacing the missing values in Age with average Age
df["Age"] = df["Age"].fillna(df["Age"].mean(), inplace = True)

# Replacing the missing values in Experiance_Years with average Experiance_years
df["Experience_Years"] = df["Experience_Years"].fillna(df["Experience_Years"].median(), inplace= True)

# or collectively replace all Nan values with there mean value of each column
df.fillna(df.mean(numeric_only = True), inplace = True)

# To remove duplicate rows
df.drop_duplicates(inplace = True)

# To remove duplicate rows with only different employee_id
df.drop_duplicates(subset = df.columns.drop("Emp_ID"), inplace = True)
print(df.shape)

# Replacing negative values with mean()
df["Salary_INR"] = np.where(df["Salary_INR"] <= 0, df["Salary_INR"].mean(), df["Salary_INR"])

# Removing rows where salary is too high or too low
salary_mean = df["Salary_INR"].mean()
salary_std = df["Salary_INR"].std()
lower_bond = salary_mean - (3 * salary_std)
upper_bond = salary_mean + (3 * salary_std)
df = df[(df["Salary_INR"] >= lower_bond) & (df["Salary_INR"] <= upper_bond)]

# Now the table is completelly cleaned its time to save it!

df.to_csv("Filtered and cleaned employyes data.csv", index = False)
print("Data cleaning completed! Saved as 'Filtered and cleaned employyes data.csv' ")