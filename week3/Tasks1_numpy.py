###########task1#################
import numpy as np
v = np.arange(10, 50)
print("Original:", v)
print("Reversed:", v[::-1])
#############task2##############
array = np.random.random((5, 5))
print("Array:\n", array)

min_value = array.min()
max_value = array.max()

print("Minimum:", min_value)
print("Maximum:", max_value)
##############task3#############
matrix = np.random.random((5, 5))

normalized = (matrix - matrix.min()) / (matrix.max() - matrix.min())
print("Normalized matrix:\n", normalized)
#############task4#############
A = np.random.random((5, 3))
B = np.random.random((3, 2))

result = np.dot(A, B)
print("Matrix A (5x3):\n", A)
print("Matrix B (3x2):\n", B)
print("Result (5x2):\n", result)
##############task5##########
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))
################task6################
array = np.random.random(10) * 100  #
print("Original:", array)

method1 = array.astype(int)

method2 = np.floor(array).astype(int)

method3 = np.trunc(array).astype(int)

method4 = np.fix(array).astype(int)

method5 = np.array([int(x) for x in array])

print("Method 1:", method1)
print("Method 2:", method2)
print("Method 3:", method3)
print("Method 4:", method4)
print("Method 5:", method5)
##############task7#####################
import numpy as np

dtype = [
    ('x', int),
    ('y', int),
    ('r', int),
    ('g', int),
    ('b', int)
]

arr = np.array([
    (10, 20, 255, 0, 0),
    (30, 40, 0, 255, 0),
    (50, 60, 0, 0, 255)
], dtype=dtype)

print(arr)