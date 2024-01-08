import pandas as pd
df = pd.read_csv('/py/Customers.csv')
print(df.query('Age > 30 and Income < 30000'))
print(df[(df["Work Experience"]>5) & (df["Profession"] == "Lawyer")])
