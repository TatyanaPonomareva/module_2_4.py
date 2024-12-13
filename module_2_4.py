numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
def is_prime(num):
    if num <2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for num in numbers:
    if num != 1:
        if is_prime(num):
            primes.append(num)
        else:
            not_primes.append(num)
print("numbers=", numbers)
print("Primes:", primes)
print("Not_primes:", not_primes)

