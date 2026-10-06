# #########task1###########
import numpy as np
#
# def numbers():
#     for i in range(1, 11):
#         yield i
# arr = np.array(list(numbers()))
#
# print(arr)
# ############task2###############
# import numpy as np
#
# A = np.random.randint(1, 10, 5)
# B = np.random.randint(1, 10, 5)
#
# print("A =", A)
# print("B =", B)
#
# if np.array_equal(A, B):
#     print("A و B برابر هستند.")
# else:
#     print("A و B برابر نیستند.")
##############task3###############
# points = np.random.rand(100, 2)
# distances=np.sqrt(np.sum(np.diff(points, axis=0) ** 2, axis=1))
# print(distances)
############task4#############
# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# mean = np.mean(A, axis=1)
# result=A-mean[:,np.newaxis]
# print(result)
######task5###########
# A = np.array([
#     [1, 8, 3],
#     [4, 2, 6],
#     [7, 5, 9]
# ])
# result=A[A[:,1].argsort()]
# print(result)
#########task6#########

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

rank = np.linalg.matrix_rank(A)

print(rank)
###########task7#############
import numpy as np

A = np.arange(1, 257).reshape(16, 16)

result = A.reshape(4, 4, 4, 4).sum(axis=(2, 3))

print(result)