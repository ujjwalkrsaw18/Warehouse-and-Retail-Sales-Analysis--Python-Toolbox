# NAME: UJJWAL KUMAR SAW
# ROLL NO: 24
# SECTION: K23EV
# COURSE CODE/TITLE: INT 373 / DATA SCIENCE TOOLBOX PYTHON PROGRAMMING

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Top 10 Items by Warehouse Sales
df = pd.read_csv("Warehouse_and_Retail_Sales.csv")

top_items = df.groupby('ITEM DESCRIPTION')['WAREHOUSE SALES'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
top_items.plot(kind='bar', color='skyblue')
plt.title("Top 10 Items by Warehouse Sales")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 2. Retail Sales by Item Type (Pie Chart)
type_sales = df.groupby('ITEM TYPE')['RETAIL SALES'].sum()

plt.figure(figsize=(8, 8))
plt.pie(type_sales, labels=type_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Retail Sales by Item Type")
plt.axis('equal')
plt.show()

# 3. Scatter Plot: Retail vs Warehouse Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='WAREHOUSE SALES', y='RETAIL SALES', hue='YEAR', palette='viridis')
plt.title("Retail vs Warehouse Sales")
plt.xlabel("Warehouse Sales")
plt.ylabel("Retail Sales")
plt.tight_layout()
plt.show()

# 4. Top 10 Item Types by Frequency
top_types = df['ITEM TYPE'].value_counts().head(10).index

plt.figure(figsize=(10, 6))
sns.countplot(data=df[df['ITEM TYPE'].isin(top_types)], y='ITEM TYPE', order=top_types)
plt.title("Top 10 Item Types by Frequency")
plt.xlabel("Count")
plt.ylabel("Item Type")
plt.tight_layout()
plt.show()

# 5. Monthly Retail Sales Trend
monthly_sales = df.groupby(['YEAR', 'MONTH'])['RETAIL SALES'].sum().reset_index()
monthly_sales['DATE'] = pd.to_datetime(monthly_sales['YEAR'].astype(str) + '-' + monthly_sales['MONTH'].astype(str))

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['DATE'], monthly_sales['RETAIL SALES'], marker='o', color='purple')
plt.title("Monthly Retail Sales Trend")
plt.xlabel("Date")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. IQR Calculation for Outlier Detection
df = pd.read_csv("Warehouse_and_Retail_Sales.csv")

numeric_columns = ['RETAIL SALES', 'RETAIL TRANSFERS', 'WAREHOUSE SALES']

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    print(f"{column}:")
    print(f"  Q1  = {Q1}")
    print(f"  Q3  = {Q3}")
    print(f"  IQR = {IQR}\n")

# 7. Boxplot: Warehouse Sales by Item Type
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='ITEM TYPE', y='WAREHOUSE SALES')
plt.title("Distribution of Warehouse Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Warehouse Sales")
plt.tight_layout()
plt.show()

# 8. Histogram of Retail Sales
sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.histplot(df['RETAIL SALES'].dropna(), bins=50, color='#FF6F61', edgecolor='black', kde=True)

plt.title("Distribution of Retail Sales", fontsize=16, fontweight='bold')
plt.xlabel("Retail Sales", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# 9. Heatmap of Monthly Retail Sales
pivot_table = df.pivot_table(index='YEAR', columns='MONTH', values='RETAIL SALES', aggfunc='sum')

plt.figure(figsize=(12, 7))
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="YlOrRd")
plt.title("Monthly Retail Sales Heatmap")
plt.xlabel("Month")
plt.ylabel("Year")
plt.tight_layout()
plt.show()

# 10. Total Sales per Year (Bar Chart)
yearly_sales = df.groupby('YEAR')[['RETAIL SALES', 'WAREHOUSE SALES']].sum().reset_index()

yearly_sales.plot(kind='bar', x='YEAR', figsize=(10, 6), color=['#FFB347', '#87CEEB'])
plt.title("Total Sales per Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 11. Monthly Retail Sales Trends by Year
plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x='MONTH', y='RETAIL SALES', hue='YEAR', marker='o', palette='tab10')
plt.title("Monthly Retail Sales Trends by Year")
plt.xlabel("Month")
plt.ylabel("Retail Sales")
plt.tight_layout()
plt.show()
