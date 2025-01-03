# -*- coding: utf-8 -*-
"""Sales Data Analysis Pandas Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kjMxoM4X3ZDzrdZcqiwdirl0VhRi9fs-
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('/content/superstore_sales.xlsx')
df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

sales_by_region = df.groupby('region')['sales'].sum()
sales_by_region

sales_by_product = df.groupby('product_name')['sales'].sum()
sales_by_product

df['Month'] = pd.to_datetime(df['order_date']).dt.month
sales_by_month = df.groupby('Month')['sales'].sum()
sales_by_month

#Calculate the profit margin
df['profit_margin'] = (df['profit'] / df['sales'])
df['profit_margin']

#Calculate the average profit margin for each product
profit_margin_by_product = df.groupby('product_name')['profit_margin'].mean().head(10)
profit_margin_by_product

#Visulaization of plot the profit margin for each product
profit_margin_by_product.plot(kind='bar')
plt.xlabel('Product')
plt.ylabel('Profit Margin')
plt.title('Profit Margin by Product')
plt.show()

#Identify the top selling product and regions
#sort the products by total sales in descending order
top_selling_products = sales_by_product.sort_values(ascending=False).head(10)
top_selling_products

#Plot top selling products
top_selling_products.plot(kind='bar')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Top Selling Products')
plt.show()

#top selling regions
#sort regions by total sales in descending order
top_selling_region = sales_by_region.sort_values(ascending = False).head(10)
top_selling_region

#plot top selling region
top_selling_region.plot(kind='bar')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.title('Top selling Region')
plt.show()