#первый факториал, количество цифр которого равно 1000
from math import ceil, log10
a, b = 0, 1
i = 0
while 1:
	i += 1
	a, b = b, a + b
	if ceil(log10(a)) == 1000: 
		break
print(i)