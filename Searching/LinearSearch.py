def linear_search(array, item):
    for i in range(0, len(array)):
        if array[i] == item:
            return i
    return -1

arr = [1, 2, 44, 12, -1, 95]
print(linear_search(arr, -11))

