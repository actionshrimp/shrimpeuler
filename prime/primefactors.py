from shrimpeuler.prime.sieves import atkin

def primefactors(n, prime_generator=None):

	if prime_generator is None:
		g = atkin(n+100)
		prime = g.next()
	else:
		g = prime_generator
		prime = g.send('reset')

	factors = dict()

	while n != 1:
		if n % prime == 0:
			try:
				factors[prime] += 1
			except KeyError:
				factors[prime] = 1

			n /= prime
		else:
			prime = g.next()

	return factors
