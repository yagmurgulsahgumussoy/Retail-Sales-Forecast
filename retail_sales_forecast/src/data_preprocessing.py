#%%
import pandas as pd
# %%
df = pd.read_csv("../data/cleaned_online_retail.csv", encoding="ISO-8859-1")

# convert datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print("data loaded.")
df.head()
# %%
df["Year"] = df["InvoiceDate"].dt.year # extract year from InvoiceDate
df["Month"] = df["InvoiceDate"].dt.month # extract month from InvoiceDate
df["Day"] = df["InvoiceDate"].dt.day # extract day from InvoiceDate
df["Hour"] = df["InvoiceDate"].dt.hour # extract hour from InvoiceDate
df["Weekday"] = df["InvoiceDate"].dt.weekday # 0=monday, 6=sunday

print("Time features extracted:")
df[["InvoiceDate", "Year", "Month", "Day", "Hour", "Weekday"]].head()
# %% 
df["CustomerID"] = df["CustomerID"].astype(int)
customer_sales = df.groupby("CustomerID")["Quantity"].sum().reset_index() # customer bazında toplam satış miktarını buluyoruz
customer_sales.columns=["CustomerID", "TotalQuantity"]
print("Top customers by quantity")
customer_sales.sort_values(by="TotalQuantity", ascending=False).head(10) # customer bazında toplam satış miktarını buluyoruz
# %%
product_sales = df.groupby("StockCode")["Quantity"].sum().reset_index() # ürün bazında toplam satış miktarını buluyoruz
product_sales.columns = ["StockCode", "TotalSold"]
product_sales["TotalSold"] = product_sales["TotalSold"].astype(int)
print("Top selling products:")
product_sales.sort_values(by="TotalSold", ascending=False).head(10) # ürün bazında toplam satış miktarını buluyoruz
# %%
import numpy as np

df["Log_UnitPrice"] = np.log1p(df["UnitPrice"]) # log dönüşümü yapıyoruz log(x+1) şeklinde

print("Original vs. Log Unit Price:")
df[["UnitPrice", "Log_UnitPrice"]].head(10) # ilk 10 satırı gösteriyoruz
# %%
