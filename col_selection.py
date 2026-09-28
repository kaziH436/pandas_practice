# series is like a row of a table 
# data frame is like a grid so a table

import pandas as pd 
df=pd.read_csv('file_name.csv')

# select single col
df['name of col']


# select multiple cols
df[['name of col'], ['hi']]

df['startcol':'endcol']
