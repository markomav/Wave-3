def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num // 2 + 1):
        if(num % i == 0):
            return False
    return True

value = int(input("Input a number to see if it is prime: "))
if isPrime(value):
    print(value,'is Prime')
else:
    print(value,'is not Prime')