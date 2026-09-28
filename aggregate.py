import pandas as pd

df=pd.read_csv("file_name.csv")

# WHOLE DF
print(df.mean(numeric_only=True))