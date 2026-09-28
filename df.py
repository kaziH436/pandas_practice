import pandas as pd

data = {"Name": ["cat", "pig", "hat"], 
        "age":[20,30,40]
    }

df=pd.DataFrame(data)
print(df)


#custom index 
df=pd.DataFrame(data, index=['employee 1','employee 2','emoloyee 3'])
print(df)
print(df['employee 1'])
print(df.iloc(0))


# add a new column
df["employer"]=["potato",'vpn','google']

#ADD A NEW ROW 
new_row=pd.DataFrame([{"Name":"sandy", "age": 28, "employer":"engineer"}], index=["moo gler"])
df=pd.concat([df, new_row])