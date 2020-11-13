import math
A = [1, 3, 2, 9, 4, 8, 10, 22, 1]
def algorithm(A):

    def Max_Heapify(A, i, heap_size):
        l = 2*i
        r = 2*i+1
        if l <= heap_size and A[l-1] > A[i-1]:
            largest = l
        else:
            largest = i
        if r <= heap_size and A[r-1] > A[largest-1]:
            largest = r
        if largest != i:
            A[i-1], A[largest-1] = A[largest-1], A[i-1]
            Max_Heapify(A, largest, heap_size)



    def Build_Max_Heap(A):
        heap_size = len(A)
        for i in range(math.floor(len(A)/2), 0, -1):
            Max_Heapify(A, i, heap_size)
        return heap_size



    def Heap(A):
        heap_size = Build_Max_Heap(A)
        for i in range(len(A), 1, -1):
            A[1-1], A[i-1] = A[i-1], A[1-1]
            heap_size = heap_size-1
            Max_Heapify(A, 1, heap_size)
        return A

    return Heap(A)