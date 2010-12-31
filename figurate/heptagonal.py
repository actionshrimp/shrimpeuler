from shrimpeuler.figurate import Polygonal

class Heptagonal(Polygonal):

	sides = 7

	def formula(self, n):
		return n*(5*n - 3) / 2.0
