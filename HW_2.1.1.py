import numpy as np

a = np.random.randint(1, 10, size=100)
b=a[a>7]
print(round(len(a)/len(b)*100),"%")
