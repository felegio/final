import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("finance_liquor_sales.csv")
cn = df.groupby(['zip_code','bottles_sold'])
print(cn.first().to_string())


plt.plot([50000, 53000], [0, 1000])
plt.title("Bottles Sold")
plt.xlabel("X - Zip Code")
plt.ylabel("y - Bottles Sold")
df.plot(kind='scatter',x='x',y='y')
plt.show()