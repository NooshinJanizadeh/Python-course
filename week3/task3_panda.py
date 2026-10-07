from operator import truediv

import pandas as pd
df=pd.read_csv("data.csv")
df=df.set_index("city")
#print(df)
# print("*************task3**********")
# print()
# df.loc[df["age"]<18, "age="]=18
# print(df)
# print("*************task4**********")
# print()
# print(df.columns)
# print(df.isnull().sum())
# print("*************task5**********")
# print()
# columns=list(df.columns)
# columns[0],columns[2]=columns[2],columns[0]
# df=df[columns]
# print(df)
# print("*************task6**********")
# print()
# lower=df["age"].quantile(0.05)
# uppers=df["age"].quantile(0.95)
# df=df[(df["age"]>=lower) & (df["age"]<=uppers)]
# print(df)
# print("*************task9**********")
# print()
# import matplotlib.pyplot as plt
# df["age"].hist()
# plt.show()
# print("*************task8**********")
# print()
# data2={
#     'avg':[17,15,16,20,13]
#        }
# df2=pd.DataFrame(data2)
# df["avg"]=df2["avg"]
# print(df)
# print("*************task10:correllation**********")
# print()
# correlation=df.corr(numeric_only=True)
# print(correlation)

# print("*************task7**********")
# print()
# mean=df["age"].mean()
# df["age"]=df["age"].fillna(mean)
# print(df)