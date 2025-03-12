import numpy as np
import time

size = 300

start = time.time()
py_matrix1 = [[i for i in range(size)]for _ in range(size)]
py_matrix2 = [[i for i in range(size)]for _ in range(size)]
dot_py_matrix =[[sum(a * b for a, b in zip(row, col)) for col in zip(*py_matrix2)] for row in py_matrix1]
end  = time.time()
print(end-start,'sec')
print(dot_py_matrix)

start = time.time()
np_matrix1 = np.array(py_matrix1)
np_matrix2 = np.array(py_matrix2)
dot_np_matrix = np.dot(np_matrix1, np_matrix2)
end  = time.time()
print(end-start,'sec')
print(dot_np_matrix)

