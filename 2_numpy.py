import numpy as np 
# Example
arr = np.array ([10,20,30,40,50])
print(arr)
print(type(arr))

# Create a 0D Array
arr0 = np.array(24)
print ('0D array is', arr0)
# Create a 1D Array
arr1 = np.array([1,2,3,4])
print ('1D array is', arr1)
# Create a 2D Array
arr2 = np.array([[1,1,1],[1,2,1]])
print ('2D array is', arr2)
# Create a 3D Array
arr3 = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]])
print ('3D array is', arr3)

# An example for each attribute is given below:
arr = np.array([[ 1, 2, 3], [ 4, 2, 5]])
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)
print("Length of one array element in bytes. : ", arr.itemsize)
print("array’s data. : ", arr.data)