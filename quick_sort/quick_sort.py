import random


def partition(list, lowest, highest):
    i = lowest
    pivot = list[lowest]

    for j in range(lowest + 1, highest + 1):
        if list[j] <= pivot:
            i += 1
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

    # A[p] <=> A[i]
    temp = list[lowest]
    list[lowest] = list[i]
    list[i] = temp

    return i


def quick_sort(list, lowest, highest):
    if lowest < highest:
        q = partition(list, lowest, highest)  # pivot's index
        quick_sort(list, lowest, q - 1)
        quick_sort(list, q + 1, highest)


list = []

for i in range(8):
    list.append(int(random.random() * 100))

print("Random list ->", list)
print("======")

partition(list, 0, len(list) - 1)
print("Partition ->", list)
print("======")

quick_sort(list, 0, len(list) - 1)
print("Quick sorted list ->", list)
