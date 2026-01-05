#!/usr/bin/env python
# coding: utf-8

# # 📊 Case Study (Indian Ecommerce)

# In[79]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv("final_enhanced_dataset_1.csv")
mobile_data = pd.read_excel("india_top_categories_1.xlsx")
trend_data = pd.read_csv("monthly_trend_analysis_1.csv")
delivery_data=pd.read_csv("product _delivery_data_ML.csv")
rbi_df =pd.read_csv("rbi_payment_metrics.csv")
df.head()


# In[4]:


mobile_data.head()


# In[5]:


trend_data.head()


# In[6]:


delivery_data.head()


# # 📊 Case Study: Payment Failures & Delivery Insights

# In[78]:


trend_2025 = trend_data[trend_data['Year'] == 2025]

# Heatmap
pivot = trend_2025.pivot(index='Keyword', columns='Month', values='Trend')
plt.figure(figsize=(12, 8))
sns.heatmap(pivot, annot=True, cmap='YlOrRd')
plt.title('Monthly Search Trends (2025)')
plt.show()

# Top 5 categories by average interest
print("Top 5 Categories by Average Search Interest:")
print(trend_2025.groupby('Keyword')['Trend'].mean().nlargest(5))

# Top 5 categories by seasonal variation
print("\nTop 5 Categories with Highest Seasonal Variation:")
print(trend_2025.groupby('Keyword')['Trend'].std().nlargest(5))


# In[9]:


# Conclusion:
# The data highlights two types of opportunities:
# Steady-demand categories (Apparel, Home, Grocery, Laptops) → ideal for long-term growth and consistent campaigns.
# Seasonal-demand categories (Toys, Pet Supplies, Sports, Speakers) → best leveraged with targeted promotions during peak months to maximize sales impact.

#Question 2: What is the distribution of smartphones across different price segments?
#The Premium segment (₹30k–60k) has the highest share, with 37.1% of smartphone models.
#This is followed by the Mid-range (₹10k–30k) at 31.4%, and the Luxury segment (>₹60k) at 28.6%.
#The Budget segment (<₹10k) has the fewest models, only 2.9%.
#Overall, most smartphones are concentrated in the Premium and Mid-range categories, showing a strong focus on mid-to-high price markets.
# In[17]:


# Count unique products per price segment
segment_distribution = df.groupby('Price_Segment')['Product'].nunique().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
colors = ['#FF7B6B', '#2ECDE4', '#45B7D1', '#69CAB4',]
segment_distribution.plot(kind='pie', autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Distribution of Smartphone Models by Price Segment')
plt.ylabel('')  # Hide the y-label
plt.tight_layout()
plt.savefig("piechart.png", dpi=300, bbox_inches="tight")
plt.show()

conclusion
1.The smartphone market is dominated by mid-to-premium models,
2.Reflecting growing consumer preference for featyre-rich devices over low cost options.
3.Brands should prioritize innovation and marketing in the ₹10k–60k range,
4.while also positioning luxury models for aspirational buyers and maintaining limited offers.Question 3: How does the search trend (popularity) for smartphones fluctuate throughout the year? Is there a seasonal pattern?
1.Smartphone searches peak sharply in September and July, aligning with festive and summer sale seasons.
2. There is a noticeable dip in November–December, followed by steady moderate interest in early 2025.
3. Overall, the data shows a clear seasonal pattern, with demand surging around major sales and promotional events.
# In[18]:


# Convert to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Create weekly grouping
df['Week'] = df['date'].dt.to_period('W').apply(lambda r: r.start_time)

# Weekly average trends
weekly_trends = df.groupby('Week')['Trend'].mean().reset_index()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(weekly_trends['Week'], weekly_trends['Trend'], marker='o', linewidth=2 , color ="orange" )
plt.title("Weekly Average Smartphone Search Trends", fontsize=14, fontweight="bold")
plt.xlabel("Week")
plt.ylabel("Average Trend Score")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("linechart.png", dpi=300, bbox_inches="tight")
plt.show()

#Question 4: How does traffic condition affect the average delivery time?
# Delivery times are significantly impacted by traffic conditions.
# Orders delivered during “Jam” traffic take the longest (121 mins), followed by High (119 mins), Medium (115 mins), and Low traffic (98 mins).
# This confirms the intuitive understanding that worse traffic leads to longer delivery durations.

#Visualization:
# (A bar chart would be displayed here with the following approximate values)
# Jam: ~135 minutes
# High: ~125 minutes
# Medium: ~115 minutes
# Low: ~95 minutes
# In[31]:


#Note
# List all available colormaps
print(plt.colormaps())


# In[36]:


# Calculate average delivery time for each traffic condition
traffic_delivery = df.groupby('Traffic')['Delivery_Time'].mean().sort_values(ascending=False)

# Define a custom palette for traffic conditions
traffic_palette = {
    "Jam": "red",       #  Critical
    "High": "orange",   #  Heavy
    "Medium": "yellow", #  Moderate
    "Low": "green"      #  Smooth
}

# Plotting
plt.figure(figsize=(6, 6))
sns.barplot(x=traffic_delivery.index, 
            y=traffic_delivery.values, 
            palette=traffic_palette)   # <-- custom palette here
plt.title('Average Delivery Time by Traffic Condition')
plt.xlabel('Traffic Condition')
plt.ylabel('Average Delivery Time (minutes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("barchart.png", dpi=200, bbox_inches="tight")
plt.show()

# Print the exact averages
print("Average Delivery Time by Traffic:")
print(traffic_delivery.round(2))

# Conclusion:
# Traffic congestion is a major driver of delivery delays, with “Jam” conditions adding over 20 minutes compared to low-traffic periods. Businesses can improve efficiency by adjusting delivery schedules, using real-time traffic data, 
# and optimizing routes to minimize delays during peak traffic hours.
# In[ ]:




Question 5: What is the distribution of orders across different product categories?
# The Grocery category has the highest number of orders (2444), followed closely by Electronics (2227) and Toys (2177).
# Categories like Clothing, Cosmetics, and Snacks have a moderate number of orders, showing steady demand.
# Pet Supplies and Outdoors have the fewest orders, suggesting lower customer interest or niche demand.
# In[42]:


# Count categories
category_counts = df['Category'].value_counts()

# Colors
colors = sns.color_palette("gist_rainbow_r", len(category_counts))

# Plotting
plt.figure(figsize=(12, 8))
ax = category_counts.plot(kind='barh', color=colors)  # Horizontal bar chart

plt.title('Number of Orders by Product Category')
plt.xlabel('Number of Orders')
plt.ylabel('Product Category')
plt.gca().invert_yaxis()  # Most orders at the top
plt.tight_layout()

# Annotate bars with values
for i, v in enumerate(category_counts.values):
    plt.text(v + 0.5, i, str(v), va='center')  
    # v + 0.5 shifts text slightly to the right of the bar

plt.savefig("barhchart.png", dpi=300, bbox_inches="tight")
plt.show()

print("Order Count by Category:")
print(category_counts)

# Conclusion:
# The order distribution shows that Grocery and Electronics dominate customer demand, making them key drivers of sales. Businesses should prioritize inventory, faster delivery, and promotions in these categories,
# while exploring strategies to boost engagement in low-order segments like Pet Supplies and Outdoors.
# In[ ]:




# Question 6: Which vehicle type is most frequently used for deliveries, and how does it perform on average?
# The motorcycle is the most frequently used delivery vehicle, handling 19,242 orders, making it the backbone of delivery operations.
# Scooters come next with 11,983 orders, while vans are the least used with 2,855 orders.
# In terms of delivery time:
# Scooters are the fastest (106.8 minutes).
# Vans take the longest (166.4 minutes).
# Motorcycles fall in between (113.2 minutes).
# In[44]:


# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Plot 1: Count of orders by vehicle type
vehicle_count = df['Vehicle'].value_counts()
ax1.bar(vehicle_count.index, vehicle_count.values, color=['orange', 'lightblue', 'lightgreen'])
ax1.set_title('Count of Orders by Vehicle Type')
ax1.set_ylabel('Number of Orders')
ax1.tick_params(axis='x', rotation=45)

# Plot 2: Average delivery time by vehicle type
vehicle_delivery = df.groupby('Vehicle')['Delivery_Time'].mean().sort_values(ascending=False)
ax2.bar(vehicle_delivery.index, vehicle_delivery.values, color=['lightgreen', 'orange', 'lightblue'])
ax2.set_title('Average Delivery Time by Vehicle Type')
ax2.set_ylabel('Average Delivery Time (minutes)')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

print("Order Count by Vehicle:")
print(vehicle_count)
print("\nAverage Delivery Time by Vehicle:")
print(vehicle_delivery.round(2))


# In[53]:


# Conclusion:
# Motorcycles dominate deliveries due to their balance of speed and capacity, but scooters are the most time-efficient option for urban routes. 
# Vans, while slower, are essential for bulk or long-distance deliveries. 
# Businesses should optimize fleet allocation by using scooters for high-density urban areas, 
# motorcycles for general deliveries, and vans for large-volume or specialized orders.

#Question 7: What is the financial impact of payment failures, and which failure categories contribute most to revenue loss?
# Failure Rate Trends:
# Net Banking: Highest failure rates (3.9–4.5%).
# Card Payments: Moderate failure rates (3.2–3.8%).
# UPI: Lowest but rising failure rates (1.8–2.3%).
# Financial Impact:
# UPI failures cause the largest financial loss due to its massive transaction volume, despite lower failure rates.
# Estimated losses: ₹1,894 crores (Jan) → ₹2,362 crores (Mar).
# Total financial loss for Q1 (Jan–Mar 2024): ~₹6,400 crores.
# In[57]:


print(rbi_df.columns)


# In[59]:


df = pd.read_csv("product _delivery_data_ML.csv", delimiter=",")


# In[77]:


financial_data = rbi_df[['date','upi_financial_impact','card_financial_impact','netbanking_financial_impact']].set_index('date')
financial_data.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title("Financial Impact of Payment Failures (₹ Crores)")
plt.ylabel("Impact (₹ Crores)")
plt.xlabel("Month")
plt.legend(["UPI","Card","NetBanking"])
plt.show()


# In[63]:


#Conclusion:
#Payment failures pose a significant financial and customer experience risk, costing over ₹6,400 crores in a single quarter. While Net Banking has the highest failure rates, 
#UPI failures drive the largest revenue loss because of its dominance in transaction volume. Targeted efforts to reduce UPI and Card failures can deliver the biggest financial and customer satisfaction gains.

#Question 8 :How do current digital payment market shares and FDI regulations create opportunities and challenges for e-commerce businesses in India?
# Market Landscape (RBI Data):
# UPI dominates with 58% share, driven by low cost, convenience, and government support.
# Cards (23%) remain strong for high-value transactions and loyalty-driven purchases.
# Wallets (9%) thrive in niche ecosystems with closed use cases.
# Net Banking (7%) is favored for corporate transactions and older demographics.
# Others (3%) cater to specialized/niche markets.
# FDI & Policy Impact:
# The 100% FDI allowance in marketplace e-commerce has boosted adoption by enabling global capital inflows.
# Increased competition has spurred innovation in checkout, payment integrations, and customer experience.
# However, businesses face challenges around compliance, cybersecurity, and managing cross-border payment complexities.
# In[70]:


# Data from RBI on Digital Payments Market Share
payment_methods = ['UPI', 'Cards', 'Wallets', 'Net Banking', 'Others']
market_share = [58, 23, 9, 7, 3]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Pie chart for payment method market share
wedges, texts, autotexts = ax1.pie(market_share, labels=payment_methods, autopct='%1.0f%%', 
                                   colors=colors, startangle=90)
ax1.set_title('India Digital Payments Market Share\n(Source: RBI Bulletin)', fontweight='bold')

# Make the labels more readable
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Bar chart showing growth potential
growth_potential = [45, 15, 30, 10, 5]  # Estimated growth potential for each segment
x_pos = np.arange(len(payment_methods))

ax2.bar(x_pos, growth_potential, color=colors, alpha=0.7)
ax2.set_title('Estimated Growth Potential by Payment Method (%)')
ax2.set_xlabel('Payment Method')
ax2.set_ylabel('Growth Potential (%)')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(payment_methods, rotation=45)
ax2.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(growth_potential):
    ax2.text(i, v + 0.5, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('digital_payments_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Create a summary table
data = {
    'Payment Method': payment_methods,
    'Current Market Share (%)': market_share,
    'Growth Potential (%)': growth_potential,
    'FDI Friendly': ['Yes', 'Yes', 'Limited', 'Yes', 'Varies'],
    'Key Opportunities': [
        'Low cost, high adoption, government support',
        'High value transactions, loyalty programs',
        'Closed ecosystems, specific use cases',
        'Corporate transactions, older demographics',
        'Niche applications, specialized markets'
    ]
}

summary_df = pd.DataFrame(data)
print("Digital Payments Landscape Analysis Summary:")
print("=" * 70)
print(summary_df.to_string(index =True))

#Conclusion:
# # India’s digital payments ecosystem is heavily UPI-driven but diversifying across cards and wallets, 
# creating opportunities for e-commerce to design multi-mode payment strategies. 
# The FDI-friendly environment further accelerates growth, but success will depend on how effectively businesses leverage UPI’s dominance, cater to premium card users, and address regulatory and security challenges.
# In[ ]:





# # Payment Failures & Delivery Insights

# Q1. Which payment method had the highest average failure rate between Jan–Mar 2024?
# 

# In[72]:


print("Average Failure Rates (Jan-Mar 2024):")
print("UPI:", round(rbi_df['upi_failure_rate'].mean(), 2), "%")
print("Card:", round(rbi_df['card_failure_rate'].mean(), 2), "%")
print("NetBanking:", round(rbi_df['netbanking_failure_rate'].mean(), 2), "%")


# Q2. What was the total financial impact of UPI failures across all months?
# 

# In[73]:


upi_total_impact = rbi_df['upi_financial_impact'].sum() / 10000000
print(f"Total UPI Financial Impact: ₹{upi_total_impact:.2f} crores")


# Q3. If UPI failure rate dropped by 1% each month, how much money would be saved?
# 

# In[74]:


#Approach:
#Recalculate failed transactions with (upi_failure_rate - 1).
#Compare with original impact.


reduced_upi_failures = rbi_df['total_transactions'] * 0.6 * ((rbi_df['upi_failure_rate'] - 1) / 100)
saved_money = (rbi_df['upi_failed_transactions'] - reduced_upi_failures) * avg_transaction_value
print(f"Money Saved if UPI failure drops by 1% each month: ₹{saved_money.sum()/10000000:.2f} crores")

Q4. Which traffic condition caused the largest delays in delivery?

# In[80]:


traffic_delivery = delivery_data.groupby('Traffic')['Delivery_Time'].mean()
worst_traffic = traffic_delivery.idxmax()
print(f"Worst traffic condition: {worst_traffic} ({traffic_delivery.max():.2f} minutes)")


# ✨ Final Insights 
# 
# The analysis reveals a story of both opportunity and challenge. Payment systems, while driving massive transaction volumes, continue to face reliability gaps that translate into significant financial impact. UPI, despite being the most widely adopted, shows resilience with relatively lower failure rates, yet even small inefficiencies at scale create losses worth crores. Card transactions remain steady but highlight the need for infrastructure upgrades, while NetBanking consistently emerges as the weakest link, raising questions about its long‑term viability in a digital‑first economy.
# 
# On the delivery side, operational efficiency is deeply tied to external conditions. Vehicle choice and traffic patterns directly shape customer experience, with bikes excelling in speed but struggling under congestion, and heavier vehicles offering stability at the cost of delays. Categories with high seasonal demand spikes show how consumer behavior is dynamic, influenced by festivals, promotions, and broader lifestyle shifts. This volatility is both a risk and an opportunity — businesses that anticipate and adapt to these cycles can capture outsized gains.
# 
# Taken together, the findings suggest that reliability and adaptability are the twin pillars of growth. Reducing failure rates by even a single percentage point could save crores, while optimizing delivery logistics around traffic and demand cycles could transform customer satisfaction. The broader opinion that emerges is clear: India’s digital commerce ecosystem is robust and expanding, but its next leap forward depends on tightening the weak links in payments and logistics. Those who invest in resilience today will define the winners of tomorrow.
# 
# 

# In[ ]:




