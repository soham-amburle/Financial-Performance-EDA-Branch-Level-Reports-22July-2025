22 July, 2025
# 💼 Finance EDA (Monthly Branch Reports)

This project performs Exploratory Data Analysis (EDA) on internal financial reports submitted monthly by regional offices of a company operating across various countries. Each row in the dataset represents one branch’s monthly report containing key metrics like revenue, expenses, profit margins, ratings, and transaction volumes.

The analysis strictly follows the structure used in previous EDA projects (FIFA, Publishing) using Python libraries: **pandas**, **numpy**, and **matplotlib**.

---

## 📁 Dataset Overview

| Column Name         | Description                                                   |
|---------------------|---------------------------------------------------------------|
| `branch_name`       | Name of the regional office or branch                         |
| `country`           | Country where the branch is located                           |
| `department`        | Department name (e.g., Sales, HR, Finance)                    |
| `revenue_eur`       | Monthly revenue in Euros                                      |
| `expenses_eur`      | Monthly expenses in Euros                                     |
| `profit_margin`     | Profit margin as a percentage                                 |
| `rating`            | Monthly branch rating (scale: 1–10)                           |
| `transaction_volume`| Number of financial transactions processed                    |
| `report_length`     | Length of the report submitted (in words or characters)       |
| `submission_date`   | Date the report was filed                                     |

---

## 🔍 Analysis Performed

- Dataset preview and structure check
- Report count by country
- Bar chart of top 10 countries by volume
- Revenue-based sorting and filtering
- Top 5 revenue-generating branches (bar chart)
- Country-specific breakdowns (e.g., India)
- Department-specific filtering (e.g., Sales)
- Sorting by transaction volume, rating, profit margin
- Boolean filtering using NumPy
- Converting subsets to NumPy arrays

---

## 📊 Visualizations

- Top 10 reporting countries (bar chart)
- Top 5 branches by revenue (bar chart)
- Department and country-level comparisons

---

## 🛠️ Tools Used

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn (imported but not used yet)

---

## ▶️ How to Run

1. Place the dataset file `finance_report.csv` in the same directory as the script.
2. Run the script:

```bash
python finance_report_eda.py
