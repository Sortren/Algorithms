def PARENT(index):
    return (index - 1) / 2


def RIGHT(parent_index):
    return 2 * parent_index + 2


def LEFT(parent_index):
    return 2 * parent_index + 1


def HEAPIFY(A, parent_index, heap_size):
    l = LEFT(parent_index)
    r = RIGHT(parent_index)

    if (l <= heap_size - 1) and (A[l] > A[parent_index]):
        largest = l
    else:
        largest = parent_index

    if r <= (heap_size - 1) and (A[r] > A[largest]):
        largest = r

    if largest != parent_index:
        # A[parent_index] <=> A[largest]
        temp = A[largest]
        A[largest] = A[parent_index]
        A[parent_index] = temp

        HEAPIFY(A, largest, heap_size)


def BUILD_HEAP(A):
    start_index = len(A) // 2 - 1
    heap_size = len(A)

    for parent_index in range(start_index, -1, -1):
        HEAPIFY(A, parent_index, heap_size)


def HEAP_SORT(A):
    BUILD_HEAP(A)
    heap_size = len(A)
    for i in range(heap_size - 1, 0, -1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        heap_size = heap_size - 1
        HEAPIFY(A, 0, heap_size)


if __name__ == '__main__':
    list = [1, 5, 6, 1, 2, 3, 6, 8, 9, 0, 12]
    print("given random list              -> ", list)

    BUILD_HEAP(list)
    print("heap built from the given list -> ", list)

    HEAP_SORT(list)
    print("Sorted list based on heap sort -> ", list)
