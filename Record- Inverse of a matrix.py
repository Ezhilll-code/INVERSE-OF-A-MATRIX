#Program to find the inverse of a matrix.
#Developed by: Ezhilan H
#RegisterNumber: 212225240040

import numpy as np

A = np.array([[6, 2, 3],
              [3, 1, 1],
              [10, 3, 4]])

det = np.linalg.det(A)

if det != 0:
    A_inv = np.linalg.inv(A)
    print(A_inv)
else:
    print("Inverse does not exist (Determinant = 0)")
