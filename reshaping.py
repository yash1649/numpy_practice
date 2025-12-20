import numpy as np

arr = np.array([3,2,4,10,0])

#sort
print("sorted: ", np.sort(arr)) #use arr.sort() to sort original array

#concatenate
a = np.array([3,2,4,10,0])
b = np.array([6,7,3,4,2])
print(np.concatenate((a,b)))

#reshape
arr2 = np.arange(27)
print(arr2.reshape(3,3,3)) #conserve the total number of elements

#adding new axis
arr3 = np.arange(3)
print(arr3)
arr3 = arr3[np.newaxis,:]
print(arr3)

arr4 = np.arange(3)
arr4 = arr4[:,np.newaxis]
print(arr4)

#expand
arr5 = np.arange(1,4)
print(np.expand_dims(arr5,1))