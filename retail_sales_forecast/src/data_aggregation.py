#%% 
import pandas as pd

df = pd.read_csv("../data/processed_online_retail.csv") # işlenmiş veriyi yüklüyoruz
# %%
df.head()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]) # InvoiceDate'i datetime formatına çeviriyoruz
df.head()
# %%

 # %% Create Year and Month columns directly
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
df.head()
# %%
# countr, product and month grouping
agg_df = df.groupby(["Country", "StockCode", "Description", "Year", "Month"])["Quantity"].sum().reset_index()

agg_df.columns = ["Country", "StockCode", "Description", "Year", "Month", "Quantity"] # kolon isimlerini değiştiriyoruz
agg_df.head(10)
# %%
agg_df.to_csv("../data/monthly_product_sales.csv", index=False)

# %%
