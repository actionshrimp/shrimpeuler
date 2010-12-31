import math

def isprime(n):

	if n == 1:
		return False
	elif n == 2:
		return True
	elif n % 2 == 0:
		return False
	else:

		flag = True
		i = 3

		while i < int(math.sqrt(n))+1 and flag:
			if n % i == 0:
				flag = False

			i += 2

		return flag

def isprime_cached(n, cache):
	cur = cache[-1]
	r = None

	while n > cache[-1]:
		if cur % 10000 == 0:
			print 'cache has reached: ' + str(cur)
		cur += 1
		r = False
		
		if isprime(cur):
			cache.append(cur)
			if cur == n:
				r = True

	if r == None:
		if n in cache:
			return True
		else:
			return False
	else:
		return r

