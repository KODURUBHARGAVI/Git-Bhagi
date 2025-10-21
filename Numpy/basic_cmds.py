import numpy as np
print(np.__version_)
print(dir(numpy)) 
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) ##gives <class 'numpy.ndarray'>
arr0 = np.array(42) #0-D array
arr1 = np.array([1, 2, 3, 4, 5]) ##1-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) ##2-D array
'''An array that has 2-D arrays (matrices) as its elements is called 3-D array
Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:'''
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr.ndim) #gies O/p as 0/1/2/3
arr = np.array([[1, 2, 3, 4],[1,2,3,4]], ndmin=5) ##ndmin Can crete array with given dimensions
print(arr[1]) ##slicing just like nested arrays--> 
arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3]) ##access elements and sum it up
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr[0,1]) ##comma sep values- first is dimension and rest related to index
arr = np.array([[[1, 2, 3], [4, 5, 6],[7,8,9]], [[7, 8, 9], [10, 11, 12],[5,6,7]],[[7, 8, 9], [10, 11, 12],[1,2,3]]])
print(arr[1,1,-2]) #negative indexing can also be used just like we use in lists, tuples etc

