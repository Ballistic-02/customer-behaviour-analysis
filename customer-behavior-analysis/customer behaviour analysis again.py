import pandas as pd
data = pd.read_csv('synthetic_customer_data.csv')
print(data.head())
print(data.info())
print(data.describe())

import matplotlib.pyplot as plt
import seaborn as sns

data.loc[data['Income_Level'] < 0, 'Income_Level'] = data['Income_Level'].median()

category_analysis = data.groupby('Product_Category').agg({
    'Total_Spending': 'mean',
    'CLV': 'mean',
    'Customer_ID': 'count'
}).rename(columns={'Customer_ID': 'Count'}).sort_values(by='Total_Spending', ascending=False)

loyalty_analysis = data.groupby('Loyalty_Member').agg({
    'Total_Spending': 'mean',
    'Purchase_Freq': 'mean',
    'CSAT_Score': 'mean',
    'CLV': 'mean'
})

churn_analysis = data.groupby('Churn_Risk').agg({
    'CSAT_Score': 'mean',
    'Total_Spending': 'mean',
    'Total_Purchases': 'mean'
})

plt.figure(figsize=(10, 6))
sns.barplot(x=category_analysis.index, y='Total_Spending', data=category_analysis, palette='viridis')
plt.title('Average Total Spending by Product Category')
plt.ylabel('Average Total Spending ($)')
plt.savefig('spending_by_category.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Loyalty_Member', y='CLV', data=data)
plt.title('CLV: Loyalty Members vs Non-Members')
plt.xticks([0, 1], ['Non-Member', 'Loyalty Member'])
plt.savefig('clv_loyalty.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.countplot(x='Churn_Risk', data=data, order=['Low', 'Medium', 'High'])
plt.title('Distribution of Churn Risk')
plt.savefig('churn_risk_distribution.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Total_Spending', hue='Gender', data=data, alpha=0.5)
plt.title('Total Spending vs Age')
plt.savefig('spending_vs_age.png')
plt.close()

print("Category Analysis:\n", category_analysis)
print("\nLoyalty Analysis:\n", loyalty_analysis)
print("\nChurn Analysis:\n", churn_analysis)

