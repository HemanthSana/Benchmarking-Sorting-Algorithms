import math
A = [2, 1, 5, 9, 11, 42, 3, 7, 13, 99]

def algorithm(A):

    def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1
    R = [0] * n2

    for i in list(range(n1)):
        L[i] = A[p + i - 1]

    for j in list(range(n2)):
        R[j] = A[q + j]

    L.append(float('inf'))
    R.append(float('inf'))

    i = 1 - 1     # Subtract 1 to adjust to Python indexing
    j = 1 - 1     # Subtract 1 to adjust to Python indexing

    for k in list(range(p - 1, r)):     # Subtract 1 from q to adjust to Python range object
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1



    def mergeSort(A, p, r):
        if p < r
        q = math.floor((p + r)/2)
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)
        return A


