from shrimpeuler.figurate import Polygonal

class Triangular(Polygonal):

	sides = 3

	def formula(self, n):
		return n*(n + 1) / 2.0

