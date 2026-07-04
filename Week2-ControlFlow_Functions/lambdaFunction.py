"""Lambda function examples for 100 days practice.

This file demonstrates simple uses of `lambda` including `map`, `filter`,
`sorted(..., key=...)`, and closures that return lambdas.
"""


def examples():
	# Simple lambda assigned to a variable
	add = lambda x, y: x + y

	# Using lambda with map and filter
	squares = list(map(lambda x: x * x, [1, 2, 3, 4]))
    #map() function applies the given function to each item of an iterable (like a list) and returns a list of the results. In this case, it squares each number in the list [1, 2, 3, 4].
	evens = list(filter(lambda x: x % 2 == 0, range(10)))
#filter() function constructs an iterator from elements of an iterable for which a function returns true. Here, it filters out the even numbers from the range 0 to 9.

	# Using lambda as key for sorting
	pairs = [(1, 'b'), (2, 'a')]
	sorted_by_str = sorted(pairs, key=lambda t: t[1])

	# Returning a lambda (closure)
	def make_multiplier(n):
		return lambda x: x * n

	double = make_multiplier(2)

