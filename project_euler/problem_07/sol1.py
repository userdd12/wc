# -*- coding: utf-8 -*-
'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the Nth prime number?
'''
from __future__ import print_function
from math import sqrt

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

def isprime(n):
    if (n==2):
        return True
    elif (n%2==0):
        return False
    else:
        sq = int(sqrt(n))+1
        for i in range(3,sq,2):
            if(n%i==0):
                return False
    return True

def solution(n):
    """Returns the n-th prime number.
 
    >>> solution(6)
    13
    >>> solution(1)
    2
    >>> solution(3)
    5
    >>> solution(20)
    71
    >>> solution(50)
    229
    >>> solution(100)
    541
    """
    i=0
    j=1
    while(i!=n and j<3):
        j+=1
        if (isprime(j)):
            i+=1
    while(i!=n):
        j+=2
        if(isprime(j)):
            i+=1
    return j

if __name__ == "__main__":
    print(solution(int(raw_input().strip())))
