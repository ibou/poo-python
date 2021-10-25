import pandas as pd
df = pd.read_csv('data.csv')
print(df.groupby(['gender','country']).mean())


df.price_paid = df.price_paid.apply(lambda x: x.replace("$", ""))
df.price_paid = df.price_paid.astype(float)
df["price_total"] = df["price_paid"] * (1 - df["tax"] / 100)
print(df["price_total"])
