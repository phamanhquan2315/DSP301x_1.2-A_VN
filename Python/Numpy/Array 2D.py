import numpy as np

a = np.array([[0,1,0],[1,0,1]])
a += 3
print(a)
b = a+3
print(a[1,2] + b[1,2])
print()
a = np.array([[3,6,7],[5,-3,0]])
b = np.array([[1,1],[2,1],[3,-3]])
c = np.dot(a,b)
print(c)
print()
a = np.array([[1,2,3],[0,1,4]])
b = np.zeros((2,3), dtype = np.int16)
print(b)