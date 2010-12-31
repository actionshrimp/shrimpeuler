def digitdistrib(n):
	digits = dict()
	for digit in str(n):
		i = int(digit)
		try:
			digits[i] += 1
		except KeyError:
			digits[i] = 1

	return digits


