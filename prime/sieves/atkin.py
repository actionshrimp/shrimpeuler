import math
import itertools

def atkin(lim):

	primes = dict.fromkeys(range(1, lim), False)

	for p in (2, 3, 5):
		primes[p] = True 

	for x in range(1, int(math.sqrt(lim)) + 1):
		for y in range(1, int(math.sqrt(lim)) + 1):
			l = 4*x*x + y*y
			if (l < lim) and l % 60 in (1, 13, 17, 29, 37, 41, 49, 53):
				primes[l] = not(primes[l])

			m = 3*x*x + y*y
			if (m < lim) and m % 60 in (7, 19, 31, 43):
				primes[m] = not(primes[m])

			if (x > y):
				n = 3*x*x - y*y
				if (n < lim) and n % 60 in (11, 23, 47, 59):
					primes[n] = not(primes[n])

	for n in range(5, int(math.sqrt(lim)) + 1):
		if primes[n]:
			i = 1
			sq = n*n
			sqmul = i*sq

			while (sqmul) < lim:
				primes[sqmul] = False
				i +=1
				sqmul = i*sq

	final_primes = set(itertools.ifilter(lambda x: primes[x], primes))
	y_num = 1

	while y_num < lim:
		setter = None
		if y_num in final_primes:
			setter = (yield y_num)

		if setter is None:
			y_num += 1
		else:
			y_num = 2

