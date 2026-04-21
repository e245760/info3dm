import numpy as np

#演習(1)
a = np.array([[1],
            [1],
            [1],
            [1],
            [1]], dtype=float)

#演習(2)
a[2, 0] = 3.14

#演習(3)
a.T

#演習(4)
np.dot(a, a.T)

#演習(5)
np.random.seed(0)
b = np.random.rand(10, 1)

#演習(6)
A = np.random.normal(loc=10, scale=2, size=(2, 5))

#演習(7)
col_1 = A[:, 2]

#演習(8)
col_2 = A[:, 3:5]

#演習(9)
B = np.random.rand(5, 2)
C = np.dot(A, B)

print(C)