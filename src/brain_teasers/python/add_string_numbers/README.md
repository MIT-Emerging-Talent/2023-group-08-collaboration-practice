# add_string_numbers.py

This module defines a function for adding two numbers represented as strings and returning the result as a string.

### Function:

```python
def add_string_numbers(num1: str, num2: str) -> str:
```

### Parameters:

num1 (str): A string representing the first number.
num2 (str): A string representing the second number.

### Returns:

str: A string representing the result of adding the two input numbers.

### Behavior:

The function attempts to convert the input strings to floating-point numbers.
It then adds the numbers and converts the result back to a string.
The result string is formatted to limit the number of decimal places to 10.
Trailing zeros and the decimal point are removed if there are no decimal places in the result.
If the input strings are not valid numeric strings, a ValueError is raised.

### Example Usage:

``` python
result = add_string_numbers("1", "2")
print(result)
# Output: "3"

result = add_string_numbers("1.1", "2.2")
print(result)
# Output: "3.3"

result = add_string_numbers("123456789", "987654321")
print(result)
# Output: "1111111110"

try:
    result = add_string_numbers("1", "abc")
except ValueError as e:
    print(f"Error: {e}")
# Output: ValueError: Invalid input: Please provide valid numeric strings
```