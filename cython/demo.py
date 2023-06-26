import demo
import numpy as np
import time

a = np.random.randn(3,4).astype(np.float32)
b = np.random.randn(4,3).astype(np.float32)

def naive_dot(a, b):
    if a.shape[1] != b.shape[0]:
        raise ValueError('shape not matched')
    n, p, m = a.shape[0], a.shape[1], b.shape[1]
    c = np.zeros((n, m), dtype=np.float32)
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(p):
                s += a[i, k] * b[k, j]
            c[i, j] = s
    return c

def demo_cython():
    re = demo.naive_dot(a, b)

def demo_python():
    re = naive_dot(a, b)

if __name__ == '__main__':
    t = time.time()
    for i in range(10):
        demo_cython()
    print(f'cython time cost = {time.time()-t}')
    t1 = time.time()
    for i in range(10):
        demo_python()
    print(f'python time cost = {time.time()-t1}')
