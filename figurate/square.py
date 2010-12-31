from shrimpeuler.figurate import Polygonal

class Square(Polygonal):

	sides = 4

	def formula(self, n):
		return n*n
