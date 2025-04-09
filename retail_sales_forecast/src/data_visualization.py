#%% import libs

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure correct working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# load the cleaned data
file_path = "../data/cleaned_online_retail.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("data loaded.")
print(df.head())


# %% total sales over time

plt.figure(figsize=(12, 6))
df.resample("M", on="InvoiceDate")["Quantity"].sum().plot() # resample ile aylık toplam satış miktarını buluyoruz
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Quantity Sold")
plt.grid(True) # grid ekliyoruz
plt.show()
# %% Sales by country

plt.figure(figsize=(12, 6))
country_sales = df.groupby("Country")["Quantity"].sum().sort_values(ascending=False).head(10) # ülke bazında toplam satış miktarını buluyoruz
sns.barplot(x=country_sales.index, y=country_sales.values, palette="viridis")  # barplot ile görselleştiriyoruz
plt.title("Top 10 contries by sales")
plt.xlabel("Country")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45) # x eksenindeki yazıları 45 derece döndürüyoruz
plt.show()

# %% Top Selling Products
plt.figure(figsize=(12, 6))
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10) # ürün bazında toplam satış miktarını buluyoruz
sns.barplot(x=top_products.values, y=top_products.index, palette="coolwarm") # barplot ile görselleştiriyoruz
plt.title("Top 10 Best Selling Products")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Description")
plt.show()

# %% Price DEscription

# fiyat ve bu fiyatta kaç ürün var
plt.figure(figsize=(12, 6))
sns.histplot(df["UnitPrice"], bins=50, kde=True, color="blue") # histogram ile fiyat dağılımını görselleştiriyoruz, fiyatları 50 gruba böl, kde=True->yoğunluk fonksiyonu
plt.title("Price Distribution")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.xlim(0, df["UnitPrice"].max()) # x eksenini sıfırdan başlatıyoruz
plt.show()
# %%
