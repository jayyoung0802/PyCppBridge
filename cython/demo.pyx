import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cdef np.ndarray[np.float32_t, ndim=2] _naive_dot(np.ndarray[np.float32_t, ndim=2] a, np.ndarray[np.float32_t, ndim=2] b):

    cdef np.ndarray[np.float32_t, ndim=2] c
    cdef int n, p, m
    cdef np.float32_t s

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


def naive_dot(a, b):
    return _naive_dot(a, b)