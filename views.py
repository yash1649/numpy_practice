import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
print(np.vstack((arr,arr2)))
print(np.hstack((arr,arr2)))

#deep copy
arr3 = np.arange(10)
arr_slice = arr3[3:6].copy()
arr_slice[0] = 999
print(arr_slice)
print(arr3)
