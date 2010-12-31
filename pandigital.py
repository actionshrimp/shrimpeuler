def ispandigital(n, min=0, max=9):
	s = str(n)
	for i in range(min, max+1):
		if str(i) not in s:
			return False

	return True
