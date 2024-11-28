"""
    Selection Sort is a sorting algorithm that sorts an  array of elements
    by choosing the largest/smallest element in the array and placing it in
    the right place.
        ADV:
            - easy to implement
            - less swaps compared to other methods which means less memory
            writes during sorting(shines when memory writes are costly)
            - O(1) memory space
        DISADV:
            - Time complexity is O(n^2), slower
            - relative order is not maintained

"""


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

"""
    Finds and replaces the smallest element for the i-th place;
    Checks the rest of the array for the smallest using j index;
    
    If there is element smaller than the element in the i-th place:
        => swaps the two elements.
        
    The direction is i: 0 => length;  j: i + 1 => length
"""
def selection_sort_smallest(array):
    for i in range(0, len(array)):
        smallest = i
        for j in range(i, len(array)):
            if array[j] < array[smallest]:
                smallest = j

        # Swap if there is less item found!
        if smallest != i:
            # swap(array, smallest, i)
            # alternative for swap method.
            array[smallest], array[i] = array[i], array[smallest]

    return array


"""
    Finds and replaces the largest element for the i-th place;
    Checks the rest of the array for the largest using j index;
    
    If there is element larger than the element in the i-th place:
        => swaps the two elements.
        
    The direction is i: length-1 => 0;  j: i - 1 => -1
    ** -1 has been added to check the first element 
    *** -1 generates numbers for loop [... , 0]
"""
def selection_sort_largest(array):
    length = len(array)
    for i in range(length-1, 0, -1):
        largest = i
        for j in range(i, 0, -1): # -1 => second element should also be checked!
            if array[j] > array[largest]:
                largest = j

        if largest != i:
            # swap(array, largest, i)
            # alternative for swap method.  
            array[largest], array[i] = array[i], array[largest]

    return array


array = [2, 3, 1, 0, -1, 98, 10, 5]
print(selection_sort_smallest(array))
print(selection_sort_largest(array))