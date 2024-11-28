"""
    1) Finding Middle element of the Array is done by:
        mid = low + (high-low) // 2

    2) The condition for binary search is:
        high >= low
    ** low -- is the starting index for search
    ** high -- is the last/end index for search
"""

def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = low + (high-low)//2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search_recursive(arr, low, mid-1, x)
        if arr[mid] < x:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1


def binary_search_iterative(arr, l, x):
    i = 0
    j = l - 1
    while j >= i:
        mid = i + (j - i) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            j = mid -1
        if arr[mid] < x:
            i = mid + 1
    return -1


arr = [-1, 0, 1, 2, 3, 43, 87, 918]
print(binary_search_recursive(arr, 0, len(arr) -1, 918))
print(binary_search_iterative(arr, len(arr), 918))