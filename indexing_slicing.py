import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr[(arr % 2 == 0) & (arr % 3 == 0)])

condition = arr < 5
print(condition)

print(np.nonzero(arr > 2))
