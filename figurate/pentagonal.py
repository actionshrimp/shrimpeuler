from shrimpeuler.figurate import Polygonal

class Pentagonal(Polygonal):

	sides = 5

	def formula(self, n):
		return n*(3*n - 1) / 2.0
