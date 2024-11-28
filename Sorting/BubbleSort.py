"""
    Bubble Sort works by looping the array and swapping if the
    two adjacent elements requires swapping. Algorithm continues
    doing that n^2 time which ensures every element touched and swapped.

    The last i elements would already be sorted, so l-i-1.


    ** Optimization for this algorithm is that if no swaps are made during
    the inner iteration that means the array is already sorted.

    ADVs:
        -- easy to implement
        -- stable (relative order is preserved)
        -- no additional memory.

    DISADVs:
        -- O(n^2) time complexity
        -- many comparisons
"""

def bubble_sort(array):
    l = len(array)
    for i in range(0, l):
        swapped = False
        for j in range(0, l-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array


array = [3, 4, 0, 7, 5, 6, 9, 2]
print(bubble_sort(array))