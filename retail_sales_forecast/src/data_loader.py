import pandas as pd

#load the csv file
file_path = "data/online_retail.csv"

# turn into csv file to dataframe
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# print the first 5 rows of the dataframe
print("\nFirst 5 row: \n", df.head())

# print the info of the dataframe
print("\nDataset Information:\n")
df.info()

"""
RangeIndex: 541909 entries, 0 to 541908
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype  
---  ------       --------------   -----  
 0   InvoiceNo    541909 non-null  object 
 1   StockCode    541909 non-null  object 
 2   Description  540455 non-null  object 
 3   Quantity     541909 non-null  int64  
 4   InvoiceDate  541909 non-null  object 
 5   UnitPrice    541909 non-null  float64
 6   CustomerID   406829 non-null  float64
 7   Country      541909 non-null  object 
dtypes: float64(2), int64(1), object(5)
"""

print("\nUnique Product Count:\n", df["Description"].nunique(dropna=True))

print("\nPrint Distrubiton:\n", df["UnitPrice"].describe())

print("\nMissing Values Summary:\n", df.isnull().sum())

