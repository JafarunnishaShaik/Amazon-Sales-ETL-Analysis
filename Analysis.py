# Yearly Sales Trend
yearly_sales = orders_df.groupby('year')['amount'].sum().reset_index()
print("Yearly Sales Trend:\n", yearly_sales)
# Monthly Sales Trend (Across All Years)
monthly_sales = orders_df.groupby('month')['amount'].sum().reset_index()
print("Monthly Sales Trend:\n", monthly_sales)
# Year-Month Sales Trend
year_month_sales = orders_df.groupby('year_month')['amount'].sum().reset_index()
print("Year-Month Sales Trend:\n", year_month_sales)