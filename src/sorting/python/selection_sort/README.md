# Selection Sort Algorithm

## Overview

This repository contains a Python implementation of the Selection Sort algorithm. Selection Sort is a simple sorting algorithm that divides the input array into a sorted and an unsorted region. The algorithm repeatedly selects the minimum element from the unsorted region and swaps it with the first element of the unsorted region, effectively expanding the sorted region.

### selection_sort.py

This module defines a function for sorting a list in accending order.

## Function Signature

```python
def selectionsort_v1(array: List[int]) -> List[int]:
    # Implementation details...
```

#### Parameters:

list (int): A list containing unordered integers


#### Returns:

list (int): A list containing ascending ordered integers 

## Behavior:

The method takes the smallest (or largest) element from the unsorted portion of the list and swaps it with the first member in the unsorted section. This method is repeated for the remaining unsorted list sections until it is completely sorted. 


## Implementation

The selection sort algorithm is implemented in the function `selectionsort_v1` defined in the file `selection_sort.py`.



## Usage

To use the selection sort algorithm, follow these steps:

* Import the selectionsort_v1 function from the selection_sort module:
```python
from selection_sort import selectionsort_v1
```
* Create an unsorted list of integers:
```python
unsorted_array = [64, 25, 12, 22, 11]
```

* Call the selectionsort_v1 function, passing the unsorted list as an argument:
```python
sorted_array = selectionsort_v1(unsorted_array)
```

The function will return a new list containing the sorted elements.


Example

```python
from selection_sort import selectionsort_v1

# Create an unsorted list
unsorted_array = [64, 25, 12, 22, 11]

# Apply selection sort
sorted_array = selectionsort_v1(unsorted_array)

# Display the sorted list
print("Sorted Array:", sorted_array)
```

#### Output:

Sorted Array: [11, 12, 22, 25, 64]


## Contributing

If you would like to contribute to this project, please follow the contribution guidelines outlined in the CONTRIBUTING.md file.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

