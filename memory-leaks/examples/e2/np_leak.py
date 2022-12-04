import numpy as np
n = 50
l = []
for i in range(n):
    array_large = np.random.choice(1000, size=(7000, 7000))
    array_small = array_large[:5, :5]
    l.append(array_small)