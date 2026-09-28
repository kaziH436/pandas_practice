import pandas as pd


#df.to_string() renders a DataFrame into a full, text-based string representation.

df = pd.read_json({"file_name.json"})
print(df.to_string())