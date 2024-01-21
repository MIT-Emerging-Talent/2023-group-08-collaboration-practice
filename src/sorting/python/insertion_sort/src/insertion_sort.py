def insertionsort_v1(arr):
    """
    Sorts the input array using the insertion sort algorithm.
    Args:
        arr (List[int]): The input array to be sorted.
    Returns:
        List[int]: The sorted array in ascending order.
    """

    for i in range(1, len(arr)):
        # Select the current element to be inserted at the correct position
        key = arr[i]
        j = i - 1
        # Initialize the index of the previous element
        j = i - 1  

        # Move elements greater than the key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
            # Shift the element to the right
            arr[j + 1] = arr[j]  
            # Move to the previous element
            j -= 1  

    return arr
        # Insert the key at the correct position
        arr[j + 1] = key  

     # Return the sorted array
    return arr 