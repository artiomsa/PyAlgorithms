#бинарный поиск по отсортированному массиву
def binsearch(item,list):
    high = len(list)-1
    low = 0
    while high >= low:
        mid = (high + low) // 2
        if list[mid] == item:
            return mid
        if list[mid] < item:
            low = mid + 1
            continue
        if list[mid] > item:
            high = mid - 1
            continue
    return None