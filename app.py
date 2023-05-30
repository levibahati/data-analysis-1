import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

#Importing the dataset
df = pd.read_csv("transaction_invoices.csv")

# Title and subtitle
st.title("Logistics Data Analysis")
st.subheader("Transaction Invoices Report")

#1. Total Revenue
total_revenue = df["invoice_amount"].sum()
st.write("Total Revenue: Ksh.", total_revenue)

#2. Total Number of Invoices
total_invoices = df["invoice_number"].nunique()
st.write("Total Number of Invoices: ", total_invoices)

#3. Average Invoice Amount
average_invoice_amount = df["invoice_amount"].mean()
st.write("Average Invoice Amount:  Ksh.", average_invoice_amount)

#4. total credit notes
total_credit_notes = df['credit_note'].nunique()
st.write("Total Credit Notes:  Ksh.", total_credit_notes)

#5. total credit note amount
total_credit_note_amount = df['credit_note_amount'].sum()
st.write("Total Credit Note Amount:  Ksh.", total_credit_note_amount)

#6. Average Credit Note Amount
average_credit_note_amount = df["credit_note_amount"].mean()
st.write("Average Credit Note Amount: Ksh.", average_credit_note_amount)

#7. Delivery Notes vs. Credit Notes
delivery_notes_count = df["delivery_note"].count()
credit_notes_count = df["credit_note"].count()
st.write("Delivery Notes:", delivery_notes_count)
st.write("Credit Notes:", credit_notes_count)

#8. top customers by invoice
top_customers_by_invoice = df.groupby('user_id')['invoice_amount'].sum().nlargest(5)
st.write("Top Customers by Invoice:  Ksh.", top_customers_by_invoice)

#9. monthly invoice trends
df['invoice_date'] = pd.to_datetime(df['invoice_date'])
monthly_invoice_trends = df.groupby(pd.Grouper(key='invoice_date', freq='M')).agg({'invoice_number': 'nunique'})
st.write("Monthly Invoice Trends:  Ksh.", monthly_invoice_trends)

#10. top customers by credit note
top_customers_by_credit_note = df.groupby('user_id')['credit_note_amount'].sum().nlargest(5)
st.write("top customers by credit note:  Ksh.", top_customers_by_credit_note)

#11. monthly credit note trends
df['dnote_date'] = pd.to_datetime(df['dnote_date'])
monthly_credit_note_trends = df.groupby(pd.Grouper(key='dnote_date', freq='M')).agg({'credit_note': 'nunique'})
st.write("Monthly Credit Note Trends:  Ksh.", monthly_credit_note_trends)

#12. total shipments
total_shipments = df['tracking_no'].nunique()
st.write("Monthly Credit Note Trends:  Ksh.", monthly_credit_note_trends)

#13. tracking update delay
# Convert date columns to datetime
df['invoice_date'] = pd.to_datetime(df['invoice_date'])
df['tracking_date'] = pd.to_datetime(df['tracking_date'])
# Calculate tracking update delay in days
df['tracking_update_delay'] = (df['tracking_date'] - df['invoice_date']).dt.days
# Display tracking update delay
st.write("Tracking Update Delay (in days):")
st.write(df['tracking_update_delay'])

#14. Additional Insights
comments_analysis = df['comments'].str.lower().str.split().explode().value_counts().head(10)
st.write("Additional Insights: ", comments_analysis)

#14. Revenue by Currency
st.subheader("Revenue vs Currency")
revenue_by_currency = df.groupby("currency_id")["invoice_amount"].sum()
st.bar_chart(revenue_by_currency)

#15. Revenue by Month
st.subheader("Revenue by Month")
df["invoice_date"] = pd.to_datetime(df["invoice_date"])
df["month"] = df["invoice_date"].dt.month
revenue_by_month = df.groupby("month")["invoice_amount"].sum()
st.line_chart(revenue_by_month)


#16. Invoice Status Distribution
st.subheader("Invoice Status Distribution")
invoice_status_distribution = df["status"].value_counts()
fig, ax = plt.subplots()
ax.pie(invoice_status_distribution, labels=invoice_status_distribution.index, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)


#17. Top Customers by Revenue
st.subheader("Top Customers by Revenue")
top_customers = df.groupby("user_id")["invoice_amount"].sum().nlargest(5)
st.bar_chart(top_customers)

#18. Invoice Count by Status
st.subheader("Invoice Count by Status")
invoice_count_by_status = df["status"].value_counts()
st.bar_chart(invoice_count_by_status)

#19. Invoice Amount Distribution
st.subheader("Invoice Amount Distribution")
fig, ax = plt.subplots()
ax.hist(df["invoice_amount"], bins=10)
ax.set_xlabel("Invoice Amount")
ax.set_ylabel("Frequency")
st.pyplot(fig)

#20. Credit Note Amount Distribution
st.subheader("Credit Note Amount Distribution")
fig, ax = plt.subplots()
ax.hist(df["credit_note_amount"], bins=10)
ax.set_xlabel("Credit Note Amount")
ax.set_ylabel("Frequency")
st.pyplot(fig)

#21. Delivery Note Count by Month
st.subheader("Delivery Note Count by Month")
df["invoice_date"] = pd.to_datetime(df["invoice_date"])
df["month"] = df["invoice_date"].dt.month
delivery_notes_by_month = df.groupby("month")["delivery_note"].count()
st.line_chart(delivery_notes_by_month)

#22. Invoice Amount by Currency
st.subheader("Invoice Amount by Currency")
invoice_amount_by_currency = df.groupby("currency_id")["invoice_amount"].sum()
st.bar_chart(invoice_amount_by_currency)

#23 Invoice Amount by User
st.subheader("Invoice Amount by User")
invoice_amount_by_user = df.groupby("user_id")["invoice_amount"].sum()
st.bar_chart(invoice_amount_by_user)

#24 Invoice Amount by Day of the Week
st.subheader("Invoice by Day of the Week")
df["invoice_day_of_week"] = df["invoice_date"].dt.dayofweek
invoice_amount_by_day_of_week = df.groupby("invoice_day_of_week")["invoice_amount"].sum()
st.line_chart(invoice_amount_by_day_of_week)

#25 Invoice Amount vs. Credit Note Amount
st.subheader("Invoice Amount vs. Credit Note Amount")
fig, ax = plt.subplots()
ax.scatter(df["invoice_amount"], df["credit_note_amount"])
ax.set_xlabel("Invoice Amount")
ax.set_ylabel("Credit Note Amount")
st.pyplot(fig)

#26. Invoice Amount by Level
st.subheader("Invoice Amount by Level")
invoice_amount_by_level = df.groupby("level")["invoice_amount"].sum()
st.bar_chart(invoice_amount_by_level)

#27. Average Invoice Amount by Currency
st.subheader("Average Invoice Amount by Currency")
avg_invoice_by_currency = df.groupby("currency_id")["invoice_amount"].mean()
st.bar_chart(avg_invoice_by_currency)

#28. Credit Note Amount Distribution
st.subheader("Credit Note Amount Distribution")
credit_note_amounts = df["credit_note_amount"].dropna()
fig, ax = plt.subplots()
ax.hist(credit_note_amounts, bins=10)
ax.set_xlabel("Credit Note Amount")
ax.set_ylabel("Frequency")
st.pyplot(fig)

#30. Invoice Amount Distribution
st.subheader("Invoice Amount by Currency")
fig, ax = plt.subplots()
ax.boxplot(df["invoice_amount"])
ax.set_ylabel("Invoice Amount")
st.pyplot(fig)

#31. Credit Note Amount by Month
st.subheader("Credit Note Amount by Month")
df["invoice_date"] = pd.to_datetime(df["invoice_date"])
df["month"] = df["invoice_date"].dt.month
credit_note_amount_by_month = df.groupby("month")["credit_note_amount"].sum()
st.line_chart(credit_note_amount_by_month)

#32. Invoice Status by Month
st.subheader("Invoice Status by Month")
invoice_status_by_month = df.groupby(df["invoice_date"].dt.month)["status"].value_counts().unstack().fillna(0)
st.bar_chart(invoice_status_by_month)

#33. Status Distribution by Currency
st.subheader("Status by Currency")
status_by_currency = df.groupby("currency_id")["status"].value_counts().unstack().fillna(0)
st.bar_chart(status_by_currency)
#34. Tracking Status Analysis
tracking_status_counts = df["status"].value_counts()
st.write("Tracking Status Analysis:")
st.write(tracking_status_counts)
