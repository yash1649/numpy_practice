import numpy as np

arr = np.array([[3,4],[6,7]])
multiplier = np.array([[2,3],[5,6]])

print(arr * multiplier)

arr2 = np.array([32,65,76,23,56,14,98])
print(arr2.max())
print(arr2.min())
print(arr2.sum())
print(arr2.prod())
print(arr2.mean())
print(arr2.std())

matrix = np.arange(1,17).reshape(4,4)
print(matrix)
print(matrix.max(axis=0))
print(matrix.max(axis=1))