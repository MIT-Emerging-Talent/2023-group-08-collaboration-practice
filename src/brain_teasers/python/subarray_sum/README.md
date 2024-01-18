### Subarray Sum Function

##### Overview

This Python function, subarray_sum, is designed to calculate and return the sum of elements in a subarray, given a list of integers and the start and end indices for summation.

#### Parameters

arr: List of integers representing the array from which the subarray sum is calculated.
start_index: Start index of the subarray for summation.
end_index: End index of the subarray for summation.

#### Return Value

Returns the sum of elements in the specified subarray.

#### Error Handling

Raises a ValueError if the provided indices are out of range.

#### Example Usage

```py
my_array = [1, 2, 3, 4, 5]

# Calculate the sum of subarray from index 1 to 3
result = subarray_sum(my_array, 1, 3)

print(result)
# Output: 9


```
