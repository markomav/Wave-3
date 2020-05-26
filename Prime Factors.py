value = int(input('Enter an integer (2 or greater): ' ))

print('The prime factors of ' + str(value) + ' are:')

factor = 2
factors = []
while factor * factor <= value:
    if value % factor:
            factor += 1
    else:
            value //= factor
            factors.append(factor)
if value > 1:
        factors.append(value)
print(factors)