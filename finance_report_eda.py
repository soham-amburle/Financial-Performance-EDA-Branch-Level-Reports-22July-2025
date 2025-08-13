# Importing required libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns  # (imported but not used yet)

# Reading the dataset
finance = pd.read_csv('finance_report.csv')

# Previewing the first 5 rows
print(finance.head())

# Printing the entire dataset (optional)
print(finance)

# Printing all column names
for col in finance.columns:
    print(col)

# Checking the shape of the dataset
print(finance.shape)

# Counting reports per country
print(finance['country'].value_counts())

# Bar chart of top 10 countries by report volume
plt.figure(figsize=(7, 7))
plt.bar(
    list(finance['country'].value_counts()[0:10].keys()),
    list(finance['country'].value_counts()[0:10]),
    color=['skyblue']
)
plt.show()

# DataFrame of branch names and their revenue
branch_revenue = finance[['branch_name', 'revenue_eur']]
print(branch_revenue.head())

# Sorting branches by revenue
branch_revenue = branch_revenue.sort_values(by='revenue_eur', ascending=False)
print(branch_revenue.head())

# Filtering high-revenue branches
top_revenue = branch_revenue[branch_revenue['revenue_eur'] > 1000000]
print(top_revenue.head())

# Bar chart of top 5 revenue-generating branches
plt.figure(figsize=(8, 5))
plt.bar(
    list(branch_revenue['branch_name'])[0:5],
    list(branch_revenue['revenue_eur'])[0:5],
    color=["blue", "orange", "green", "red", "purple"]
)
plt.show()

# Top 3 highest-revenue branches
print(branch_revenue[0:3])

# Printing all branch names
print(finance[['branch_name']])

# Boolean: Is country India?
print(finance['country'] == 'India')

# 🇮🇳 Reports from India
India = finance[finance['country'] == 'India']
print(India.head(10))

# Highest revenue branches in India
print(India.sort_values(by='revenue_eur', ascending=False).head())

# Print all column names again
for col in finance.columns:
    print(col)

# Iterate through a string
for char in 'India and Germany':
    print(char)

# Looping through a list
for dept in ['Sales', 'HR', 'Finance']:
    print(dept)

# Looping through dictionary keys
for key in {'a': 1, 'b': 2}:
    print(key)

# Highest transaction volumes in India
print(India.sort_values(by='transaction_volume', ascending=False).head())

# 🇮🇳 Top 5 Indian branches by profit margin
print(
    India[['branch_name', 'profit_margin']]
    .sort_values(by='profit_margin', ascending=False)
    .head()
)

# Check for a specific branch-country combination
print(
    np.sum(
        (finance['country'] == 'USA') &
        (finance['branch_name'] == 'New York Central')
    )
)

# USA branches excluding a specific one
print(
    np.sum(
        (finance['country'] == 'USA') &
        (finance['branch_name'] != 'New York Central')
    )
)

# Same branch name in other countries
print(
    np.sum(
        (finance['country'] != 'USA') &
        (finance['branch_name'] == 'New York Central')
    )
)

# Number of unique countries
print(len(finance['country'].unique()))

# Convert top 5 profit-margin branches in India to NumPy array
print(
    India[['branch_name', 'profit_margin']]
    .sort_values(by='profit_margin', ascending=False)
    .head()
    .to_numpy()
)

# Same using .values
print(
    India[['branch_name', 'profit_margin']]
    .sort_values(by='profit_margin', ascending=False)
    .head()
    .values
)

# Sorting India branches by report length
print(India.sort_values(by='report_length', ascending=False).head())

# DataFrame with ratings
branch_ratings = finance[['branch_name', 'rating']]
print(branch_ratings.sort_values(by='rating', ascending=False).head())

# Ratings with department and country
rating_data = finance[['branch_name', 'rating', 'country', 'department']]
print(rating_data.sort_values(by='rating', ascending=False).head())

# Data for Sales department
sales = finance[finance['department'] == 'Sales']

# Top 5 Sales branches by revenue
print(sales.sort_values(by='revenue_eur', ascending=False).head())

# Top 5 Sales branches by rating
print(sales.sort_values(by='rating', ascending=False).head())

# Top 5 Sales branches by profit margin
print(sales.sort_values(by='profit_margin', ascending=False).head())

# 🌍 Most common countries in Sales department
print(sales['country'].value_counts()[0:2])

