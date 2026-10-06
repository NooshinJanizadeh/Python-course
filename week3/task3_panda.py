import pandas as pd
#######task1
df = pd.read_csv("data.csv")
#########task2
df = df.set_index("city")
print(df)
