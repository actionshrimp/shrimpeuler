class Polygonal(object):

	def __init__(self):
		pass

	def formula(self, n):
		raise NotImplementedError

	def generator(self, min=None, lim=None):

		n = 1
		val = 1
		while (val < lim) or (lim == None):
			setter = None
			if (val >= min) or (min == None):
				setter = (yield val)

			if setter is not None:
				n = setter
			else:
				n += 1

			val = int(self.formula(n))

	@classmethod
	def withsides(self, sides):
		for c in self.__subclasses__():
			if c.sides == sides:
				return c
