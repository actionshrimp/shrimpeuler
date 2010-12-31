from shrimpeuler.prime import primefactors

def totient(n, prime_factors=None):
	if prime_factors is None:
		pf = primefactors(n)
	else: 
		pf = prime_factors

	return int(round(reduce(lambda x, y: x * (1 - 1./y), [n] + pf.keys())))

