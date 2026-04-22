from data_preprocessing import load_data
from eda import plot_sales, plot_profit
from statistical_analysis import correlation, average_sales, max_sales

# Load dataset
df = load_data()

# Show first rows
print(df.head())

# Visualization
plot_sales(df)
plot_profit(df)

# Statistical Analysis
print("Average Sales:", average_sales(df))
print("Max Sales:", max_sales(df))
print("Correlation:", correlation(df))