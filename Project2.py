# ============================================================
#  DATA WRANGLING PROJECT - Online Retail Dataset
# Author: Kholod
# Description: Cleaning and preparing online retail data for analysis
# ============================================================

# -----------------------------
# 1. Import Required Libraries
# -----------------------------
from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd

# # -----------------------------
# # 2. Load Dataset
# # -----------------------------
# df = pd.read_csv(
#     r"C:\Users\kholod\Desktop\My Python\data.csv",  # dataset path
#     encoding="latin1",                              # fix encoding issues
#     parse_dates=["InvoiceDate"]                     # parse date column
# )

# # -----------------------------
# # 3. Initial Data Overview
# # -----------------------------
# print("===== Original Data Info =====")
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.head())

# # -----------------------------
# # 4. Clean Column Names
# # -----------------------------
# # remove any leading/trailing spaces from column names
# df.columns = df.columns.str.strip()

# # -----------------------------
# # 5. Handle Missing Values
# # -----------------------------
# df["Description"] = df["Description"].fillna("Unknown")  # replace missing product descriptions
# df["CustomerID"] = df["CustomerID"].fillna(-1)           # temporary fill for missing customer IDs

# # -----------------------------
# # 6. Remove Duplicates & Invalid Rows
# # -----------------------------
# df = df.drop_duplicates()            # remove duplicate rows
# df = df[df["Quantity"] > 0]          # keep only positive quantities
# df = df[df["UnitPrice"] > 0]         # keep only positive prices
# df = df[df["CustomerID"] > 0]        # remove placeholder customers (-1)

# # -----------------------------
# # 7. Convert Data Types
# # -----------------------------
# df["CustomerID"] = df["CustomerID"].astype(int)
# df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
# df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

# # -----------------------------
# # 8. Create New Features
# # -----------------------------
# # calculate total price per transaction
# df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# # extract date/time features
# df["InvoiceYear"] = df["InvoiceDate"].dt.year
# df["InvoiceMonth"] = df["InvoiceDate"].dt.month
# df["InvoiceDay"] = df["InvoiceDate"].dt.day
# df["InvoiceHour"] = df["InvoiceDate"].dt.hour
# df["Weekday"] = df["InvoiceDate"].dt.day_name()

# # -----------------------------
# # 9. Check Data After Cleaning
# # -----------------------------
# print("===== Cleaned Data Info =====")
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.head())

# # -----------------------------
# # 10. Basic Analysis
# # -----------------------------
# # total sales per country
# country_sales = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False)

# # total monthly sales
# monthly_sales = df.groupby(["InvoiceYear", "InvoiceMonth"])["TotalPrice"].sum()

# # top 10 best-selling products
# top_products = df.groupby("Description")["TotalPrice"].sum().sort_values(ascending=False).head(10)

# # -----------------------------
# # 11. Export Cleaned Data
# # -----------------------------
# df.to_csv(r"C:\Users\kholod\Desktop\My Python\FinalVersion.csv", index=False)

# print("Data cleaning and export completed successfully!")

# -----------------------------
# 12. Anallysing with Matpotlib 
# -----------------------------

x = [1 , 2, 3, 4, 5, 6, 7]
y = [40 , 80 , 70 , 50 , 30 , 20 , 100]
z = [10 , 20 , 30 , 40 , 50 , 60 , 70]
plt.plot(x , y  , color = 'blue' , linestyle = '--' , marker = '*' , linewidth = 3 , label = 'l1')
plt.plot(x , z , color = 'black' , linestyle = '-.' , marker = '.' , linewidth = 2 , label = 'l2')
plt.title("Training")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
# plt.colorbar('blue')
plt.show()

