import pandas as pd 
# Load the dataset
wages = pd.read_csv('Wages.csv')
# Display the first 10 rows
print(wages.head(10))
# Display the last 10 rows
print(wages.tail(10))
# How many rows are in the DataFrame
print(len(wages))
# Display metadata for the DataFrame
print(wages.info())
# Display the data types for two columns from the dataset
print(wages.dtypes[['age', 'wage']])
# Display the column names from the dataset
print(wages.columns.tolist())
# Display the DataFrame’s index
print(wages.index)
# How many individual elements are in the DataFrame?
print(wages.size)
# How many columns and rows are there?
rows, columns = wages.shape
# Display descriptive statistics for the wage column, and the age column
wage_stats = wages['wage'].describe()
age_stats = wages['age'].describe()
# print(wage_stats, age_stats)

# Display descriptive statistics for the wage and age columns, by each race
grouped = wages.groupby('race')['wage', 'age'].describe()
# print(grouped)

# What do the mean and median values of wage tell us about the data?
mean = wages['wage'].mean()
median = wages['wage'].median()

# Display the age and wage columns only
columns = wages[['age', 'wage']]
print(columns)
# Are these two columns correlated?
correlation = wages[['age', 'wage']].corr()
print(correlation)
# Display the top 10 salaries
top_10 = wages.nlargest(10, 'wage')
print(top_10)
# Display the counts of each race in the dataset
counts = wages['race'].value_counts()
print(counts)
# Display the proportion of each race in the dataset
proportions = wages['race'].value_counts(normalize=True)
print(proportions)
# Create a bar plot of regional proportionality
import matplotlib.pyplot as plt

region_counts = wages['region'].value_counts()
region_counts.plot(kind='bar')
plt.title('Regional Proportionality')
plt.xlabel('Region')
plt.ylabel('Count')
plt.show()