from shrimpeuler.figurate import Polygonal

class Hexagonal(Polygonal):

	sides = 6

	def formula(self, n):
		return n*(2*n -1)
