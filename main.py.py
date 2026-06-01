# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:36:45 2026

@author: Tech zone
"""

import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
# load the main sales data file
df = pd.read_csv("online_retail_II.csv", sep=",")

# task 1
# find out which columns have missing blank spaces
missing_counts = df.isna().sum()
cols_with_missing_vals = missing_counts[missing_counts > 0]
print("Columns with missing values are:\n Name       Missing vals")
print(cols_with_missing_vals)

# remove rows where the customer id is blank
MainSales = df.dropna(subset=['Customer ID'])
print(f"missing vals in customerId after cleaning it:{MainSales['Customer ID'].isna().sum()}")

# fill in any missing dates using the value right above them
MainSales['InvoiceDate'] = MainSales['InvoiceDate'].ffill()
print(f"missing vals after filling the invoice date column:{MainSales['InvoiceDate'].isna().sum()}")

# split the data into returned items and actual sales
returns_df = MainSales[MainSales['Quantity'] < 0].copy()
MainSales = MainSales[MainSales['Quantity'] >= 0].copy()
print(f"Minimum quantity in main sales df is now: {MainSales['Quantity'].min()}")
print(f"Maximum quantity in returns sales df is now: {returns_df['Quantity'].max()}")

# change date column text into a proper date format
MainSales['InvoiceDate'] = pd.to_datetime(MainSales['InvoiceDate'])
returns_df['InvoiceDate'] = pd.to_datetime(returns_df['InvoiceDate'])
print("InvoiceDate column data type in MainSales df:", MainSales['InvoiceDate'].dtype)
print("InvoiceDate column data type in Returns Sales df:", returns_df['InvoiceDate'].dtype)

# task 2
# multiply how many items were bought by their price to get total spent
MainSales['Total_Spent'] = MainSales['Quantity'] * MainSales['Price']
print(f"after calclating total spent:\n{MainSales[['Quantity', 'Price', 'Total_Spent']].head()}")

# pull out the month and the name of the day from the date
MainSales['Month'] = MainSales['InvoiceDate'].dt.month
MainSales['DayOfWeek'] = MainSales['InvoiceDate'].dt.day_name()
print(f"after extracting day and month from date:\n{MainSales[['InvoiceDate', 'Month', 'DayOfWeek']].head()}")

# find the top countries based on row count
top_10 = MainSales['Country'].value_counts().nlargest(10).index.tolist()

# group countries together into wider regions
region_map = {
    'United Kingdom': 'UK',
    'Germany': 'Europe',
    'France': 'Europe',
    'EIRE': 'Europe',
    'Spain': 'Europe',
    'Netherlands': 'Europe',
    'Belgium': 'Europe',
    'Switzerland': 'Europe',
    'Portugal': 'Europe',
    'Australia': 'Rest of World'
}

# apply the regional group names and label any leftovers as rest of world
MainSales['Region'] = MainSales['Country'].map(region_map).fillna('Rest of World')

# task 3
# add up everything each customer spent and pick the top 5
customer_spending = MainSales.groupby('Customer ID')['Total_Spent'].sum()
top5customer = customer_spending.nlargest(5)
print("Top 5 Customers by Total Spent:\n", top5customer)

# make a grid table showing the average spent for each day and month combination
heatmap_data = MainSales.pivot_table(values='Total_Spent', index='DayOfWeek', columns='Month', aggfunc='mean')

# plot the grid data as a line chart and add titles
heatmap_data.plot(kind='line', marker='o')
plt.title('Average Total Spent by Day of the Week across Months')
plt.xlabel('Month of Year')
plt.ylabel('Average Total Spent (£)')
plt.legend(title='Day of Week', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('task3_sales_trends.png')
plt.close()  
print("Task 3 line graph generated and saved successfully as 'task3_sales_trends.png'.")

# calculate the average item price for each broad region
regional_prices = MainSales.groupby('Region')['Price'].mean()
print("Average Unit Price per Region:\n", regional_prices)

# task 4
# find out how far each order size is from the average score
MainSales['Quantity_ZScore'] = np.abs(stats.zscore(MainSales['Quantity']))

# separate huge abnormal orders from normal everyday ones
outliers = MainSales[MainSales['Quantity_ZScore'] > 3]
normal_sales = MainSales[MainSales['Quantity_ZScore'] <= 3]

# make a scatter plot showing normal sales in blue and outliers in red
plt.scatter(normal_sales['Quantity'], normal_sales['Price'], color='blue', label='Normal')
plt.scatter(outliers['Quantity'], outliers['Price'], color='red', label='Outliers')
plt.title('Outlier Detection')
plt.xlabel('Quantity')
plt.ylabel('Unit Price')
plt.legend()
plt.savefig('task4_outlier_scatter.png')

# separate the money spent into uk shoppers and european shoppers
uk_spend = MainSales[MainSales['Region'] == 'UK']['Total_Spent']
europe_spend = MainSales[MainSales['Region'] == 'Europe']['Total_Spent']

# run a mathematical check to see if the two group averages are truly different
t_stat, p_value = stats.ttest_ind(uk_spend, europe_spend, equal_var=False)
print(f"T-Statistic value: {t_stat:.4f}")
print(f"Calculated P-Value: {p_value:.4f}")

# print our final decision based on the mathematical threshold score
if p_value < 0.05:
    print("Conclusion: Reject H0. There is a statistically significant difference in the average Total_Spent between the UK and the rest of Europe.")
else:
    print("Conclusion: Fail to reject H0. There is no statistically significant difference in the average Total_Spent between the UK and the rest of Europe.")
    
overall_average = MainSales['Total_Spent'].mean()
print(f"overall average spend per row: £{overall_average:.2f}")

# 2. check the averages split up by country region (uk vs europe vs rest of world)
regional_averages = MainSales.groupby('Region')['Total_Spent'].mean()
print("\naverage spend broken down by region:")
print(regional_averages)