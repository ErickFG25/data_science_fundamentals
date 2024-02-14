import numpy as np 
# Example
arr = np.array ([10,20,30,40,50])
print("Numpy array")
print(arr)
print(type(arr))

print("\n------------\n")
print("Array dimensions")
# Create a 0D Array
arr0 = np.array(24)
print ('0D array is\n', arr0)
# Create a 1D Array
arr1 = np.array([1,2,3,4])
print ('1D array is\n', arr1)
# Create a 2D Array
arr2 = np.array([[1,1,1],[1,2,1]])
print ('2D array is\n', arr2)
# Create a 3D Array
arr3 = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]])
print ('3D array is\n', arr3)

print("\n------------\n")
print("Array attributes")
# An example for each attribute is given below:
arr = np.array([[ 1, 2, 3], [ 4, 2, 5]])
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)
print("Length of one array element in bytes. : ", arr.itemsize)
print("array’s data. : ", arr.data)

print("\n------------\n")
print("Array conversions")
# Example: Converting a 1D Array to a 2D Array
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Reshape")
newarr = arr.reshape(4,3)
print (newarr) 

# Converting a multidimensional(3D) array into a 1D array
print("Flatten")
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
flattened_array = arr3D.flatten()
print(flattened_array)

# Let's create a 2D array for the transpose example
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
# Transposing the 2D array
print("Transpose")
transposed_array = arr2D.transpose()
print(transposed_array)

print("\n------------\n")
print("Arithmetic operations")
# Perform element-wise addition of two arrays using the 'np.add' method
a = np.array([30,20,10])
b = np.array([1,2,3])
result = np.add (a,b)
print("Addition ", result)
result = np.subtract (a,b)
print("Substraction ", result)
result = np.multiply (a,b)
print("Multiplication ", result)
result = np.divide (a,b)
print("Division ", result)
c = np.power(a,b)
print("Power of", c)