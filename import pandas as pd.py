import pandas as pd

#MAKE SURE TO OPEN VIA ANACONDA!!

q = r"C:\Users\glass\OneDrive\Documents\Coding Class\2021\SimpliLearn_practice\testing nhl goalies.xlsx"
df = pd.read_excel(q)
print(df.head())

x = df[['Name', 'W']]
print(x)

print(df.iloc[1, 2])