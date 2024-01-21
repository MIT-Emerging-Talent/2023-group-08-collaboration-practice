def insertionsort_v1(arr):
    """
    Sorts the input array using the insertion sort algorithm.
    Args:
        arr (List[int]): The input array to be sorted.
    Returns:
        List[int]: The sorted array in ascending order.
    """

    for i in range(1, len(arr)):
        key = arr[i]  # Select the current element to be inserted at the correct position
        j = i - 1  # Initialize the index of the previous element

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift the element to the right
            j -= 1  # Move to the previous element

        arr[j + 1] = key  # Insert the key at the correct position

    return arr  # Return the sorted array