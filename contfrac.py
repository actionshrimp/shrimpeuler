from math import sqrt
from itertools import cycle

def contfrac_sqrt(n):
	root = int(sqrt(n))
	m = [0]; d = [1]; a = [root]

	def stop():
		for i in xrange(len(a) - 1):
			if (m[i], d[i], a[i]) == (m[-1], d[-1], a[-1]):
				return True

		return False

	zerodiv = False
	while not stop() and not zerodiv:
		try:
			m.append(d[-1]*a[-1] - m[-1])
			d.append((n - m[-1]**2) / d[-1])
			a.append(int((root + m[-1]) / d[-1]))
		except ZeroDivisionError:
			zerodiv = True

	if zerodiv:
		return a[0], a[1:]
	else:
		return a[0], a[1:-1]


def convergent(n, start, rep):
	l = [start]
	if rep:
		g = cycle(rep)
		while n > 1:
			l.append(g.next())
			n -= 1

		num = 1
		den = 0
		for i in reversed(l):
			t = num
			num = den
			den = t
			num += den*i

		return [num, den]

	return False

