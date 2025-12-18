import numpy as np

#restrictions
#1. all elements must be of same type
#2. cant change size of the array
#3. data must be rectangular (same number of columns)

#creating array from a list
ages = np.array([4,5,26,7,2])
print(ages)

#random content
arrempt = np.empty((3,3))
print(arrempt)

#default values
#zeros
arr  = np.zeros((3,4))
print(arr)

#ones
arr1 = np.ones((3,4))
print(arr1)

#custom
arr2 = np.full((3,4),5)
print(arr2)

# sequences of numbers
arr3 = np.arange(1,10,2)
print(arr3)

# creating identity matrices
identity_matrix = np.eye(5)
print(identity_matrix)

#linearly spaced arrays
print(np.linspace(0,20,5))