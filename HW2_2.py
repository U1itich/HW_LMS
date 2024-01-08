import pandas as pd
df = pd.DataFrame({'id':range(1,8),'age':range(1,50,7),'name':['John','Smith','Carl','Alex','Ann','Jane','Kate']})

print(df.head(3))
print(df.tail(3))

df.to_csv("C:/py/DataFrame.csv")
