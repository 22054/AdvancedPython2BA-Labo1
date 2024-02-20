from scipy.integrate import quad
from math import sqrt

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n<0:
		raise ValueError
	f = 1
	for i in range(2, n+1):
		f *= i
	return f

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta = b**2 - 4*a*c
	if delta < 0:
		return tuple()
	if delta == 0:
		rep = -b/(2*a)
		return tuple([rep])
	if delta > 0:
		rep1 = (-b+sqrt(delta))/(2*a)
		rep2 = (-b-sqrt(delta))/(2*a)
		if rep1 > rep2:
			temp = rep1
			rep1 = rep2
			rep2 = temp
		return tuple([rep1, rep2])

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower' and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	if function.find('x') == -1:
		return
	if lower > upper:
		return
	rep, _ = quad(lambda x: eval(function, {'x':x}), lower, upper)
	return round(rep, 10)

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
