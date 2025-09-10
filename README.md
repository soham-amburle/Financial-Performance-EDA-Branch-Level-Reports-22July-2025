![Power BI](https://img.shields.io/badge/Tool-Power%20BI-yellow) ![Python](https://img.shields.io/badge/Language-Python-blue)

**Date:** 22 July, 2025  
# Finance EDA – Monthly Branch Reports

This project focuses on performing Exploratory Data Analysis (EDA) on internal financial reports submitted each month by the company’s regional offices operating across different countries. Each row in the dataset represents a single branch’s monthly performance report and includes key financial and operational metrics such as revenue, expenses, profit margins, ratings, and transaction volumes.

The analysis was done using Python, following a structure similar to previous projects (such as FIFA and Publishing EDA). The primary libraries used include `pandas`, `numpy`, and `matplotlib`.

---

## Dataset Description

The dataset contains the following columns:

| Column Name          | Description                                                   |
|----------------------|---------------------------------------------------------------|
| `branch_name`        | Name of the regional office or branch                         |
| `country`            | Country where the branch is located                           |
| `department`         | Department name (e.g., Sales, HR, Finance)                    |
| `revenue_eur`        | Monthly revenue in Euros                                      |
| `expenses_eur`       | Monthly expenses in Euros                                     |
| `profit_margin`      | Profit margin as a percentage                                 |
| `rating`             | Monthly branch rating (on a scale from 1 to 10)               |
| `transaction_volume` | Number of financial transactions processed                    |
| `report_length`      | Length of the report submitted (in words or characters)       |
| `submission_date`    | Date when the report was submitted                            |

---

## Analysis Highlights

Here’s a summary of the key steps and insights generated through the analysis:

- Initial data preview and structure check to ensure data integrity
- Count of reports submitted by each country
- Bar chart showing the top 10 countries by number of reports submitted
- Filtering and sorting based on revenue
- Visualization of the top 5 revenue-generating branches
- Country-level breakdowns, with a closer look at specific countries like India
- Filtering by department, such as isolating data for the Sales team
- Sorting based on metrics like transaction volume, rating, and profit margin
- Applying boolean filtering using NumPy for conditional analysis
- Converting filtered dataframes into NumPy arrays for additional processing

---

## Visual Outputs

The following charts were created as part of the analysis:

- Bar chart of the top 10 countries based on report submission volume
- Bar chart highlighting the top 5 branches by revenue
- Department-wise and country-wise comparisons for deeper insights

---

## Tools and Libraries

- Python 3.x
- pandas
- numpy
- matplotlib  
*(Note: seaborn was imported but not used in this version of the script as it was not needed)*

---

