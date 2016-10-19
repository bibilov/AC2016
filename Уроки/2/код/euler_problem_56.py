digits_sum_list = []

for a in range(3, 100):
    for b in range(3, 100):
        digits_sum = sum([int(digit) for digit in str(a**b)])
        digits_sum_list.append(digits_sum)

print(max(digits_sum_list))
