# Product of Array Except Self

## Overview
This Python module provides a function to calculate the product of all elements in an array except the element at each corresponding index. The function takes an input array of integers and returns a new array where each element is the product of all elements in the input array except the element at the corresponding index.

## Installation
No installation is required for this module. Simply include the `array_product.py` file in your project.

## Usage

```python
from src.array_product import product_of_array_except_self

# Example
input_array = [1, 2, 3, 4, 5]
output = product_of_array_except_self(input_array)
# Expected output: [120, 60, 40, 30, 24]
