import numpy as np


arr=np.array([1,2,3,4,5])
print(arr)

print(arr.shape)
print(arr.ndim)

print(np.__version__)
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.shape)
print(arr2.ndim)
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)
print(arr3.shape)
print(arr3.ndim)