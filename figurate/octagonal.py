from polygonal import Polygonal

class Octagonal(Polygonal):

	sides = 8

	def formula(self, n):
		return n*(3*n - 2)
