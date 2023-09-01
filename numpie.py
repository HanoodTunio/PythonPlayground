import numpy as np

print(np.__version__) # checking numpy version

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) #The array object in NumPy is called ndarray. create a NumPy ndarray object by using the array() function.\


# the ndim attribute returns the number of dimensions in array 
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# creating a array with data type string 
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
