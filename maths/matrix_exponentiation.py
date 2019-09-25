"""Matrix Exponentiation"""

import timeit

"""
Matrix Exponentiation is a technique to solve linear recurrences in logarithmic time.
You read more about it here: 
http://zobayer.blogspot.com/2010/11/matrix-exponentiation.html
https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
"""


class Matrix(object):
	def __init__(self, arg):
		if isinstance(arg,list): #Initialzes a matrix identical to the one provided.
			self.t = arg
			self.n = len(arg)

		else: #Initializes a square matrix of the given size and set the values to zero.
			self.n = arg
			self.t = [[0 for _ in range(self.n)] for _ in range(self.n)]

	def __mul__(self, b):
		c = Matrix(self.n)

		for i in range(self.n):
			for j in range(self.n):
				for k in range(self.n):
					c.t[i][j] += self.t[i][k]*b.t[k][j]

		return c

def modular_exponentiation(a, b):
	ret = Matrix([[1,0], [0,1]])

	while b > 0:
		if b&1:
			ret = ret*a

		a = a*a
		b >>= 1

	return ret

def fibonacci_with_matrix_exponentiation(n, f1, f2):
	
	#Trivial Cases
	if n == 1:
		return f1

	if n == 2:
		return f2

	a = Matrix([[1,1], [1,0]])

	m = modular_exponentiation(a, n-2)

	return f2*m.t[0][0] + f1*m.t[0][1]

def simple_fibonacci(n, f1, f2):

	#Trival Cases
	if n == 1:
		return f1

	if n == 2:
		return f2

	fn_1 = f1
	fn_2 = f2

	n -= 2

	while n > 0:
		fn = fn_1 + fn_2

		fn_2 = fn_1
		fn_1 = fn

		n -= 1

	return fn

def matrix_exponentiation_time():
	setup = '''
from random import randint
from __main__ import fibonacci_with_matrix_exponentiation
'''

	code = '''
n = randint(1,70000)

f1 = 1
f2 = 1


fibonacci_with_matrix_exponentiation(n, f1, f2)
'''
	exec_time = timeit.timeit(setup = setup,
						  stmt = code,
						  number = 100)

	print ("With matrix exponentiation the average execution time is ", exec_time/100)


def simple_fibonacci_time():
	setup = '''
from random import randint
from __main__ import simple_fibonacci
'''

	code = '''
n = randint(1,70000)

f1 = 1
f2 = 1


simple_fibonacci(n, f1, f2)
'''
	exec_time = timeit.timeit(setup = setup,
						  stmt = code,
						  number = 100)

	print ("Without matrix exponentiation the average execution time is ", exec_time/100)

	
def main():
	matrix_exponentiation_time()
	simple_fibonacci_time()


if __name__ == "__main__":
	main()