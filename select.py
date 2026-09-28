import pandas as pd

df=pd.read_csv("file_name.csv",index_col="Name")

#selection row by label
print(df.loc["Pikachu"])

print(df.iloc[0:11:2]) # start:end:step for rows

print(df.iloc[0:11:2, 0:3]) # start:end:step for rows, 0:3 for cols 