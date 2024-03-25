import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.ticker as mticker
df = pd.read_csv("/Users/rahuldas/Desktop/Tortilla Dataset/tortilla_prices.csv")

print(df.head)
print(df.info()) 
print(df.shape)
print(df.columns)
print(df.dtypes)
print("hello world")
price_per_kilogram_missing = df["Price per kilogram"].isna().sum()
print(price_per_kilogram_missing)


price_per_kilogram_missing_mean = df["Price per kilogram"].mean()
print(price_per_kilogram_missing_mean)
df["Price per kilogram"] = df["Price per kilogram"].fillna(price_per_kilogram_missing_mean)
print(df["Price per kilogram"].isna().sum())
sns.set_style("whitegrid")
sns.kdeplot(data=df, x="Price per kilogram", hue="Store type", fill=True)
#plt.show()
fig, ax = plt.subplots(figsize=(6, 6))
# drawing the plot
sns.boxplot(data=df, x = "Store type", y = "Price per kilogram", color = "lightblue", ax=ax);
plt.xticks(rotation=90)
sns.despine(left=True, right=True, top=True, bottom=True)
plt.show()
ax = sns.lineplot(x = "Year", y = "Price per kilogram", data = df, hue = "Store type");
ax.xaxis.set_major_locator(mticker.MultipleLocator(3))
plt.show()
df2 = pd.read_csv("/Users/rahuldas/Desktop/Tortilla Dataset/wfp_food_prices_mex.csv", skiprows=[1])
print(df2.head)
print(df2.info())
df2["date"] = pd.to_datetime(df2["date"])
print(df2.info())
df2['Year'] = pd.DatetimeIndex(df2['date']).year
print(df2.columns)

print(df.head())
print(df2.head()) 
df_combined = pd.merge(df, df2, on="Year", how="outer")
df_combined.to_csv("DF1_COMBINED.csv")

