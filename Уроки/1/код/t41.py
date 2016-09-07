import itertools

#проверка на простое число
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d ** 2 <= n and n % d != 0:
        d += 2
    return d ** 2 > n

#вернет самое большое простое пан-число
def getMaxPrPand(s):
	for n in range(10,1,-1):
		for i in itertools.permutations(s,n):
			if isPrime(int(''.join(i))):
				return (''.join(i))

print(getMaxPrPand("7654321"))


