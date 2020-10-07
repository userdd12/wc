"""
Problem:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers which
is less than N.
"""


def solution(n: int = 998001) -> int:
    """Returns the largest palindrome made from the product of two 3-digit
    numbers which is less than n or -1 if no such product exists.

    >>> solution(20000)
    19591
    >>> solution(30000)
    29992
    >>> solution(40000)
    39893
    >>> solution(10000)
    -1
    """
    # fetches the next number
    for number in range(n - 1, 9999, -1):

        # converts number into string.
        str_number = str(number)

        # checks whether 'str_number' is a palindrome.
        if str_number == str_number[::-1]:

            divisor = 999

            # if 'number' is a product of two 3-digit numbers
            # then number is the answer otherwise fetch next number.
            while divisor != 99:
                if (number % divisor == 0) and (len(str(number // divisor)) == 3.0):
                    return number
                divisor -= 1
    return -1


if __name__ == "__main__":
    print(solution(int(input().strip())))
