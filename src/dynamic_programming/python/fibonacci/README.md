# Fibonacci Calculator

This repository contains Python functions to calculate Fibonacci numbers using different methods: recursion, basic iteration, and creating a list.

## Functions

### 1. Recursive Fibonacci

The `fib_recursion` function calculates the Fibonacci of a non-negative integer using recursion.

```python
def fib_recursion(n: int) -> int:
    # ... function details ...
```

1. Basic Iterative Fibonacci
   The fib_basic function calculates the Fibonacci of a non-negative integer using basic iteration.

```python
def fib_basic(n: int) -> int:
    # ... function details ...
```

1. List-based Fibonacci Series
   The fib_list function generates a list of Fibonacci numbers up to a specified non-negative integer.

```python
def fib_list(n: int) -> int:
    # ... function details ...
```

## Usage:

from fibonacci_calculator import fib_recursion, fib_basic, fib_list

# Calculate Fibonacci using recursion

result_recursion = fib_recursion(5)
print(f"Fibonacci (Recursion): {result_recursion}")

# Calculate Fibonacci using basic iteration

result_basic = fib_basic(5)
print(f"Fibonacci (Basic Iteration): {result_basic}")

# Generate Fibonacci series as a list

result_list = fib_list(5)
print(f"Fibonacci Series (List): {result_list}")
