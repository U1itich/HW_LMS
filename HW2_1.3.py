import numpy as np
a=np.arange(100).reshape(10,10) % np.full((10,10),10) + np.full((10,10),1)
print(a)
