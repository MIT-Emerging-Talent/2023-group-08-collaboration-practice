def fib_recursion(n: int) -> int:
    """Calculate fibonacci of a number

    Args:
        n (int): a non-negative integer that fibonacci is calculated for.

    Returns:
        int: fibonacci of n.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursion(n - 2) + fib_recursion(n - 1)


def fib_basic(n: int) -> int:
    """Calculate fibonacci of a number

    Args:
        n (int): a non-negative integer that fibonacci is calculated for.

    Returns:
        int: fibonacci of n.
    """
    a = 0
    b = 1
    count = 0
    while (count < n):
        temp = b
        b = temp + a
        a = temp
        count +=1
    return a


def fib_list(n: int) -> list:
    """returns a list of fibonacci number up to n

    Args:
        n (int): a non negative integer

    Returns:
        list: list of fibonacci numbers
    """
    fib_series = [0,1]
    while len(fib_series)<n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series