import numpy as np
c=[]
def A(a,b):
    return len(a)/len(b)
for i in range(1000):
    a = np.random.randint(1, 10, size=100)
    b=a[a>7]
    c.append(round(A(b,a)*100))

c = np.array(c)
d=c[c>20]
print(A(d,c)))
