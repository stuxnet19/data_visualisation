import pandas as pd

df = pd.read_csv("avocado.csv")

print("\n\n======> afficher les premiere ligne di data frame \n\n")
print(df.head())
print("\n\n======> afficher la colone AveragePrice \n\n")
print(df["AveragePrice"].head())