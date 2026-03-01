import pandas as pd
data = pd.read_csv('synthetic_customer_data.csv')
data['Last_Purchase_Date'] = pd.to_datetime(data['Last_Purchase_Date'])
print("--- Data Summary ---")
print(data[['Age', 'Total_Spending', 'Avg_Order_Value', 'CSAT_Score']].describe())

category_revenue = data.groupby('Product_Category')['Total_Spending'].sum().sort_values(ascending=False)
print("\n--- Revenue by Category ---")
print(category_revenue)

loyalty_stats = data.groupby('Loyalty_Member')['CSAT_Score'].mean()
print("\n--- Average Satisfaction (1=Loyalty, 0=Non-Loyalty) ---")
print(loyalty_stats)

import matplotlib.pyplot as plt

data['Churn_Risk'].value_counts().plot(kind='bar', color=['green', 'orange', 'red'])
plt.title('Customer Churn Risk Distribution')
plt.xlabel('Risk Level')
plt.ylabel('Number of Customers')
plt.show()
