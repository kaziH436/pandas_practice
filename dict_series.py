# filter using a dict
import pandas as pd

calories={"Day 1":1750, "Day 2": 2100, "Day 3": 1700}

series=pd.Series(calories)
print(series)
print(series['Day 1'])
 
series['Day 1']+=200
print(series['Day 1'])

print(series[series>2000])