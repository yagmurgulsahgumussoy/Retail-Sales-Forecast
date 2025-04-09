#%%
import pandas as pd
from sklearn.preprocessing import LabelEncoder # string verileri sayısal verilere çeviriyoruz XGBoost sadece sayısal verilerle çalışır.
from sklearn.model_selection import train_test_split # veriyi train ve test olarak ayırıyoruz
from xgboost import XGBRegressor 
from sklearn.metrics import mean_squared_error, mean_absolute_error # hata oranlarını hesaplıyoruz
import numpy as np

# %%
df = pd.read_csv("../data/monthly_product_sales.csv")

# Encode categorical features
label_cols = ["Country", "StockCode", "Description"] # string kolonları sayısal verilere çeviriyoruz
for col in label_cols:
    df[col] = LabelEncoder().fit_transform(df[col]) 

features = ["Country", "StockCode", "Description", "Year", "Month"] # özelliklerimizi belirliyoruz
target = "Quantity"

X = df[features]
y = df[target]

# time-based split: train -> 2010-2011, tes-> last 2months
train_mask = (df["Year"] < 2011) | ((df["Year"] == 2011) & (df["Month"] < 10))
X_train = X[train_mask]
y_train = y[train_mask]
X_test = X[~train_mask]
y_test = y[~train_mask]

# %%
# TRAIN AND EVALUATE XGBOOST MODEL !!!11

model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42) # modelimizi tanımlıyoruz
# n_estimators: ağaç sayısı, learning_rate: öğrenme oranı, max_depth: ağaç derinliği, random_state: rastgelelik

model.fit(X_train, y_train) # modelimizi eğitiyoruz

y_pred = model.predict(X_test) # test verisiyle tahmin yapıyoruz

#evaluate model
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) # RMSE hesaplıyoruz
mae = mean_absolute_error(y_test, y_pred) # MAE hesaplıyoruz

print(f"RMSE: {rmse:.2f}") # RMSE'yi yazdırıyoruz
print(f"MAE: {mae:.2f}") # MAE'yi yazdırıyoruz

# RMSE: 223.94 Modelin tahminlerinin ortalama 84.35 adet hata payı ile gerçekleştiğini gösterir.
# MAE: 84.35 modelin yaptığı hataların karelerinin ortalamasının kareköküdür. -> (tahmin-gerçek)^2




# %%
