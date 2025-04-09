import pandas as pd

file_path = "data/online_retail.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Drop rows with missing 'Description' values
df = df.dropna(subset = ["Description"])

# Remove negative or zero price values
df = df[df["UnitPrice"]>0]

# Drop rows with missing CustomerID (optional)
df = df.dropna(subset = ["CustomerID"])

# Remove extreme price outliers (we will set a threshold at the 99th percentile)
# ekstra yüksek ve düşük fiyatlar var, bunlar test için veya hata ile girilmiş olabilir. %99!luk orana bakıyoruz, yani fiyatlardan en uç %1'lik kısmını temizliyoruz.
# modele yanlış veri vermemek için
upper_limit = df["UnitPrice"].quantile(0.99)
df = df[df["UnitPrice"] <= upper_limit]

df.to_csv("data/cleaned_online_retail.csv", index=False)

# Print summary
print("\n🔹 Cleaned Data Overview:", flush=True)
print(df.info())

print("\n🔹 Unique Product Count:", df["Description"].nunique(dropna=True))

print("\n🔹 Price Distribution After Cleaning:")
print(df["UnitPrice"].describe())

print("\n🔹 Missing Values After Cleaning:")
print(df.isnull().sum())