MAX_DIGIT = 2000000

primes_list = [2]

for i in range(3, MAX_DIGIT, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in primes_list:
        if j*j-1 > i:
            primes_list.append(i)
            break
        if i % j == 0:
            break
    else:
        primes_list.append(i)

print(sum(primes_list))
