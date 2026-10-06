import pandas as pd
#######task1
df = pd.read_csv("data.csv")
#########task2
df = df.set_index("city")
print(df)
#########task3####
#df.loc[df["age"] < 18, "Age"] = 18
#print(df)
#########task4#######
#print(df.columns)
#print(df.isnull().sum())
#########task5#########
