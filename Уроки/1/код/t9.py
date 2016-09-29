from math import sqrt

#вернет произведение пифагорейских чисел, чья сумма равна 1000
def getMulThPifo():
	for a in range(1,1000):
		for b in range(1,1000):
				c = sqrt(a**2+b**2)
				if a + b + c == 1000:
					return int(a*b*c)

print(getMulThPifo())