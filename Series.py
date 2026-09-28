import pandas as pd

data=[100,200,300]
series = pd.Series(data) # the dtype is based on elements
print(series)


# custom index 
series = pd.Series(data, index=['a','b','c'])

#to update the value
series.loc["c"]=200


# location by label(index)
print(series.loc['a'])

#location by integer postion
print(series.iloc[1])

# index if custom needs to be the same number as the elements in the table
# e.g. index=['a','b','c'] and data=[100,200,300,400] will result in a value


