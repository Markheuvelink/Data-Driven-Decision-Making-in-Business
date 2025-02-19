# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:09:57 2023

@author: jbrweelden
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data and adjust formatting

df = pd.read_csv('Week 2.csv')
print(df)

# Combine 'Month' and 'Year' columns into a single 'Date' column
df['Date'] = pd.to_datetime(df['Month'] + ' ' + df['Year'].astype(str))

print(df)

# Format the 'Date' column to display only year and month
df['Year-Month'] = df['Date'].dt.strftime('%Y-%m')

print(df)

# Delete the "date" colummn
df = df.drop('Date', axis=1)

#############################################

# Create a Pivot table to summarize amount of deliveries per site

# Summarize data using Pivot by Site
pivot_df = df.pivot_table(index=['Site','Year-Month'], columns='Supplier', values=['Purchase value'], aggfunc='mean') 

# Print the pivoted DataFrame
print("\nPivoted DataFrame:")
print(pivot_df)

# Get unique groups for the x-axis
groups = pivot_df.index.get_level_values('Site')

# Plot using Matplotlib
pivot_df.plot(kind='bar', stacked=True)