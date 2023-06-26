from build.func import matrix_multiply
import numpy as np

a = np.random.randn(1,2).astype(np.float32)
b = np.random.randn(2,1).astype(np.float32)
print('a = {}'.format(a))
print('b = {}'.format(b))
re = matrix_multiply(a, b)
re = np.array(re)
print('re = {}'.format(re))