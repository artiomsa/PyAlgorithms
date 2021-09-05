import random


def QuickSort(array):
    if len(array) < 2:
        return array
    pivot = random.randint(0, len(array)-1)
    less = [i for i in array[1:] if i <= array[pivot]]
    greater = [i for i in array[1:] if i > array[pivot]]
    return QuickSort(less) + [array[pivot]] + QuickSort(greater)
