# ==============================
# 📊 Finance EDA – Branch Reports
# ==============================

# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style="whitegrid")

# ==============================
# 1. Load & Inspect Dataset
# ==============================
finance = pd.read_csv("finance_report.csv")

print("Dataset Shape:", finance.shape)
print("\nColumn Names:", list(finance.columns))
print("\nPreview:")
print(finance.head())

# Basic summary statistics
print("\nSummary Statistics:")
print(finance.describe())

# Missing values check
print("\nMissing Values:")
print(finance.isnull().sum())

# ==============================
# 2. Helper Functions
# ==============================

def plot_bar(data, x, y, title, xlabel, ylabel, color="skyblue", top_n=10):
    """
    Generic bar plotter for top N categories.
    """
    plt.figure(figsize=(8, 5))
    sns.barplot(x=x, y=y, data=data.head(top_n), palette=sns.color_palette("Blues", n_colors=top_n))
    plt.title(title, fontsize=14, weight="bold")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def top_n(df, column, n=5, ascending=False):
    """
    Return top N rows based on a column.
    """
    return df.sort_values(by=column, ascending=ascending).head(n)

# ==============================
# 3. Country-Level Insights
# ==============================

# Reports per country
country_counts = finance["country"].value_counts().reset_index()
country_counts.columns = ["country", "report_count"]

print("\nTop 10 Countries by Report Volume:")
print(country_counts.head(10))

plot_bar(
    country_counts,
    x="country",
    y="report_count",
    title="Top 10 Countries by Report Submissions",
    xlabel="Country",
    ylabel="Number of Reports"
)

# ==============================
# 4. Branch-Level Revenue Insights
# ==============================

branch_revenue = finance[["branch_name", "revenue_eur"]].sort_values(by="revenue_eur", ascending=False)

print("\nTop 5 Revenue-Generating Branches:")
print(branch_revenue.head())

plot_bar(
    branch_revenue,
    x="branch_name",
    y="revenue_eur",
    title="Top 5 Branches by Revenue",
    xlabel="Branch",
    ylabel="Revenue (EUR)",
    top_n=5
)

# ==============================
# 5. Country Deep-Dive (India Example)
# ==============================

india = finance[finance["country"] == "India"]

print("\nTop 5 Indian Branches by Revenue:")
print(top_n(india, "revenue_eur", 5))

print("\nTop 5 Indian Branches by Profit Margin:")
print(top_n(india, "profit_margin", 5))

print("\nTop 5 Indian Branches by Transaction Volume:")
print(top_n(india, "transaction_volume", 5))

# ==============================
# 6. Department-Level Insights
# ==============================

sales = finance[finance["department"] == "Sales"]

print("\nTop 5 Sales Branches by Revenue:")
print(top_n(sales, "revenue_eur", 5))

print("\nTop 5 Sales Branches by Rating:")
print(top_n(sales, "rating", 5))

print("\nTop 5 Sales Branches by Profit Margin:")
print(top_n(sales, "profit_margin", 5))

# ==============================
# 7. Correlation Analysis
# ==============================

plt.figure(figsize=(8, 6))
corr = finance[["revenue_eur", "expenses_eur", "profit_margin", "transaction_volume", "rating"]].corr()
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Heatmap of Key Metrics", fontsize=14, weight="bold")
plt.show()

# ==============================
# 8. Distribution Analysis
# ==============================

plt.figure(figsize=(7, 4))
sns.histplot(finance["profit_margin"], kde=True, bins=30, color="teal")
plt.title("Distribution of Profit Margins", fontsize=14, weight="bold")
plt.xlabel("Profit Margin (%)")
plt.ylabel("Frequency")
plt.show()

# ==============================
# End of Analysis
# ==============================
