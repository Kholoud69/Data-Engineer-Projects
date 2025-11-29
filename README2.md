# Online Retail Data Wrangling Project

## Overview
This project focuses on **cleaning, preparing, and analyzing** an Online Retail dataset. The dataset contains transactional data including product descriptions, quantities, prices, invoice dates, and customer information. The goal is to ensure data quality and make it ready for further analysis or visualization.

## Author
- Kholod

## Dataset
The dataset includes the following key columns:
- `InvoiceNo` – Invoice number
- `StockCode` – Product code
- `Description` – Product description
- `Quantity` – Number of items purchased
- `InvoiceDate` – Date of the transaction
- `UnitPrice` – Price per item
- `CustomerID` – Unique identifier for customers
- `Country` – Customer's country

---

## Project Workflow

### 1. Data Loading
- The dataset is loaded using **Pandas** with proper date parsing and encoding handling.

### 2. Data Cleaning
- Column names are stripped of leading/trailing spaces.
- Missing values are handled:
  - `Description` missing values are replaced with `"Unknown"`.
  - `CustomerID` missing values temporarily filled for processing.
- Duplicate rows and invalid entries are removed:
  - Only positive `Quantity` and `UnitPrice` are kept.
  - Placeholder or missing `CustomerID`s are removed.

### 3. Data Transformation
- Data types are converted:
  - `CustomerID` → integer
  - `Quantity` and `UnitPrice` → numeric
- New features are created:
  - `TotalPrice` = `Quantity` × `UnitPrice`
  - Date features: `InvoiceYear`, `InvoiceMonth`, `InvoiceDay`, `InvoiceHour`, `Weekday`

### 4. Analysis
- Total sales per country
- Monthly sales trends
- Top 10 best-selling products

### 5. Visualization
Sample plot using **Matplotlib**:

```python
x = [1, 2, 3, 4, 5, 6, 7]
y = [40, 80, 70, 50, 30, 20, 100]
z = [10, 20, 30, 40, 50, 60, 70]
```
plt.plot(x, y, color='blue', linestyle='--', marker='*', linewidth=3, label='l1')
plt.plot(x, z, color='black', linestyle='-.', marker='.', linewidth=2, label='l2')
plt.title("Training")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

Requirements

Python 3.x

Libraries:

pandas

numpy

matplotlib

Install libraries with:

pip install pandas numpy matplotlib

How to Run

Clone the repository:

git clone https://github.com/your-username/your-repo.git


Update the CSV dataset path in the script.

Run the Python script:

python your_script_name.py


The script will clean the data, perform analysis, generate plots, and export the cleaned CSV.
