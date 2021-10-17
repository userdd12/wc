"""
Calculating fibonacci numbers using matrix form and repeated squaring.
https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
"""

PRIME = 30011


def matmul(matrix_a: list, matrix_b: list) -> list:
    """
    >>> matmul([[1, 0], [0, 1]], [[1, 0], [0, 1]])
    [[1, 0], [0, 1]]
    """
    result = list()
    for i in range(len(matrix_a)):
        result.append(list())
        for j in range(len(matrix_b[0])):
            column = [x[j] for x in matrix_b]
            result[i].append(dot(matrix_a[i], column))
    return result


def dot(vector_x: list, vector_y: list) -> list:
    """
    >>> dot([1,2,3,4,5], [1,1,1,1,1])
    15
    """
    result = 0
    for xi, yi in zip(vector_x, vector_y):
        result += xi * yi
    return result % PRIME


def square(matrix_a: list) -> list:
    """
    >>> square([[1, 0], [0, 1]])
    [[1, 0], [0, 1]]
    """
    return matmul(matrix_a, matrix_a)


def power(matrix_x: list, n: int) -> list:
    """
    >>> power([[1, 0], [0, 1]], 1)
    [[1, 0], [0, 1]]
    >>> power([[1, 0], [0, 1]], 5)
    [[1, 0], [0, 1]]
    >>> power([[1, 0], [0, 1]], 10)
    [[1, 0], [0, 1]]
    """
    if n < 0:
        return matrix_x
    if n == 0:
        return [[1, 0], [0, 1]]
    if n == 1:
        return X
    if n % 2 == 0:
        return square(power(matrix_x, n / 2))
    if n % 2 != 0:
        return matmul(square(power(matrix_x, (n - 1) / 2)), matrix_x)


def fib_repeated_squaring(n: int) -> int:
    """
    >>> fib_repeated_squaring(1)
    1
    >>> fib_repeated_squaring(5)
    5
    >>> fib_repeated_squaring(10)
    55
    """
    if n == 0:
        return 0
    magic_mat = [[1, 1], [1, 0]]
    f1_f0 = [[1], [0]]
    magic_mat = power(magic_mat, n - 1)
    result = matmul(magic_mat, f1_f0)
    return result[0][0]
