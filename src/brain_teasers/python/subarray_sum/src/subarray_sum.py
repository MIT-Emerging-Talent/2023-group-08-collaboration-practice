def subarray_sum(arr: list, start_index: int, end_index: int) -> int:
    """
    Calculate and return  the sum of elements in a subarray from start_index to end_index (inclusive).
    Args:
    - arr: List of integers to be summed
    - start_index: Start pointing of summation
    - end_index: End point of summation

    Returns:
    - sum of the sub arrays from start index to end index.
    """
    # Check if the indices are valid
    if start_index < 0 or end_index >= len(arr) or start_index > end_index:
        raise ValueError("Indices out of range")
    


    # Calculate the sum of the subarray
    # pointer to keep the summation
    subarray_sum = 0
    # we add end_index+1, because  in range function, it excluded the end point. 
    for i in range(start_index, end_index + 1):
        subarray_sum += arr[i]

    return subarray_sum
