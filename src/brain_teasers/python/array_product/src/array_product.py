def product_of_array_except_self(nums):
    """
    Given an array nums of n integers, return an array output such that output[i] is equal to the product of all the
    elements of nums except nums[i].

    Args:
        nums (List[int]): The input array.

    Returns:
        List[int]: The output array where each element is the product of all elements in the input array except
        the element at the corresponding index.
    """
    if not nums:
        return []

    n = len(nums)

    # Initialize output array with 1s
    output = [1] * n

    # Calculate products of elements to the left of each index
    left_product = 1
    for i in range(n):
        output[i] *= left_product
        left_product *= nums[i]

    # Calculate products of elements to the right of each index and multiply with existing product
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output
