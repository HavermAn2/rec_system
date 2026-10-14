

import numpy as np


# ==============================
# 1. ARRAY CREATION
# ==============================

# Create a NumPy array from a Python list
arr = np.array([1, 2, 3, 4, 5])
print("np.array:", arr)

# Create an array with values from 0 to 9
a = np.arange(10)
print("np.arange:", a)

# Create an array from 1 to 10 with step 2
b = np.arange(1, 10, 2)
print("np.arange with step:", b)

# Create 5 evenly spaced numbers from 0 to 1
c = np.linspace(0, 1, 5)
print("np.linspace:", c)

# Create an array filled with zeros
zeros = np.zeros((2, 3))
print("np.zeros:")
print(zeros)

# Create an array filled with ones
ones = np.ones((2, 3))
print("np.ones:")
print(ones)

# Create an array filled with a specific value
full = np.full((2, 3), 7)
print("np.full:")
print(full)

# Create an identity matrix
eye = np.eye(3)
print("np.eye:")
print(eye)


# ==============================
# 2. ARRAY INFORMATION
# ==============================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Get array shape: rows and columns
print("shape:", matrix.shape)

# Get number of dimensions
print("ndim:", matrix.ndim)

# Get total number of elements
print("size:", matrix.size)

# Get data type of elements
print("dtype:", matrix.dtype)


# ==============================
# 3. RESHAPING
# ==============================

x = np.arange(12)

# Change shape from 1D array to 3x4 matrix
reshaped = x.reshape(3, 4)
print("reshape:")
print(reshaped)

# Convert matrix back to 1D array
flat = reshaped.flatten()
print("flatten:", flat)


# ==============================
# 4. INDEXING AND SLICING
# ==============================

arr2 = np.array([10, 20, 30, 40, 50])

# Get first element
print("first element:", arr2[0])

# Get last element
print("last element:", arr2[-1])

# Get elements from index 1 to 3
print("slice 1:4:", arr2[1:4])

m = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Get second row
print("second row:", m[1, :])

# Get third column
print("third column:", m[:, 2])

# Get element from row 2 and column 3
print("element [1, 2]:", m[1, 2])


# ==============================
# 5. MATH OPERATIONS
# ==============================

p = np.array([1, 2, 3])
q = np.array([4, 5, 6])

# Element-wise addition
print("p + q:", p + q)

# Element-wise subtraction
print("p - q:", p - q)

# Element-wise multiplication
print("p * q:", p * q)

# Element-wise division
print("q / p:", q / p)

# Power operation
print("p ** 2:", p ** 2)

# Add scalar to every element
print("p + 10:", p + 10)


# ==============================
# 6. AGGREGATION FUNCTIONS
# ==============================

nums = np.array([5, 10, 16, 20, 25])

# Sum of all elements
print("sum:", np.sum(nums))

# Mean value
print("mean:", np.mean(nums))

# Maximum value
print("max:", np.max(nums))

# Minimum value
print("min:", np.min(nums))

# Standard deviation
print("std:", np.std(nums))

# Index of maximum value
print("argmax:", np.argmax(nums))

# Index of minimum value
print("argmin:", np.argmin(nums))


# ==============================
# 7. AXIS EXAMPLES
# ==============================

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Sum of each column
print("sum axis=0:", np.sum(data, axis=0))

# Sum of each row
print("sum axis=1:", np.sum(data, axis=1))

# Mean of each column
print("mean axis=0:", np.mean(data, axis=0))

# Mean of each row
print("mean axis=1:", np.mean(data, axis=1))


# ==============================
# 8. BOOLEAN FILTERING
# ==============================

values = np.array([1, 5, 7, 2, 9, 3])

# Create boolean mask
mask = values > 5
print("mask:", mask)

# Select only values greater than 5
print("values > 5:", values[values > 5])

# Select values between 2 and 9
print("2 < values < 9:", values[(values > 2) & (values < 9)])


# ==============================
# 9. RANDOM FUNCTIONS
# ==============================

# Set seed for reproducible random numbers
np.random.seed(42)

# Random floats from 0 to 1
print("random rand:", np.random.rand(5))

# Random matrix 3x3
print("random matrix:")
print(np.random.rand(3, 3))

# Random integers from 1 to 99
print("random integers:")
print(np.random.randint(1, 100, size=(3, 3)))

# Random values from normal distribution
print("normal distribution:")
print(np.random.randn(5))


# ==============================
# 10. MATRIX OPERATIONS
# ==============================

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Matrix multiplication
print("A @ B:")
print(A @ B)

# Matrix multiplication using dot
print("np.dot(A, B):")
print(np.dot(A, B))

# Transpose matrix
print("A transpose:")
print(A.T)

# Determinant of matrix
print("det(A):", np.linalg.det(A))

# Inverse matrix
print("inverse A:")
print(np.linalg.inv(A))


# ==============================
# 11. SORTING AND UNIQUE VALUES
# ==============================

unsorted = np.array([3, 1, 5, 2, 3, 1])

# Sort values
print("sorted:", np.sort(unsorted))

# Get unique values
print("unique:", np.unique(unsorted))


# ==============================
# 12. CONCATENATION
# ==============================

arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

# Join arrays
print("concatenate:", np.concatenate([arr_a, arr_b]))

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

# Stack matrices vertically
print("vstack:")
print(np.vstack([m1, m2]))

# Stack matrices horizontally
print("hstack:")
print(np.hstack([m1, m2]))


# ==============================
# 13. RECOMMENDER SYSTEM EXAMPLE
# ==============================

# Rows are users, columns are movies
ratings = np.array([
    [5, 4, 0],
    [3, 0, 2],
    [4, 5, 1]
])

# Convert integers to floats because NaN works only with float arrays
ratings_float = ratings.astype(float)

# Replace zeros with NaN
ratings_float[ratings_float == 0] = np.nan

# Calculate average movie rating ignoring NaN
movie_avg = np.nanmean(ratings_float, axis=0)

print("movie averages:", movie_avg)


# ==============================
# 14. SIMPLE NEURON EXAMPLE
# ==============================

# Input features
x = np.array([1, 2, 3])

# Weights
w = np.array([0.5, 0.2, 0.8])

# Bias
b = 1

# Neuron output: weighted sum + bias
y = x @ w + b

print("neuron output:", y)