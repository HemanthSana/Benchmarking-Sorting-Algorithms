import math
import numpy as np


def algorithm(A):


    def Partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    def quicksort(A, p, r, _random = False):
        partition = Partition
        if _random:
            partition = Randomized_partition
        if p<r:
            q = partition(A, p, r)
            quicksort(A, p, q-1, _random)
            quicksort(A, q+1, r, _random)
        return(A)


    def Randomized_partition(A, p, r):
        m = np.random.randint(p, r+1)
        A[r], A[m] = A[m], A[r]
        return Partition(A, p, r)

    return quicksort(A, 0, len(A)-1, True)


