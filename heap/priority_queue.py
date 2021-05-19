import heap as hp


def HEAP_EXTRACT_MAX(heap):
    heap_size = len(heap)

    if heap_size < 1:
        raise ValueError('Heap is empty')

    max = heap[0]

    heap[0] = heap[heap_size - 1]
    heap_size = heap_size - 1
    hp.HEAPIFY(heap, 0, heap_size)

    return max


list = [4, 6, 7, 123, 5, 7, 56, 2]
hp.BUILD_HEAP(list)
print("Heap -> ", list)

print("Max element -> ", HEAP_EXTRACT_MAX(list))
print("Heap after removing max element -> ", list)
