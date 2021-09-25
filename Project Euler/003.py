
from math import sqrt

num = input('Enter a number to determine if it is Prime. \n')
num = int(num)
empty = []


def all_factors(num, factors):
    for i in range(1, sqrt(num)):
        if num % i == 0:
            factors.append(i)
    return factors


def is_prime(factors):
    prime = True
    if len(factors) > 1:
        prime = False
    return prime


def is_prime_num(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def largest_prime(factors):
    factors.reverse()
    for i in range(len(factors)):
        prime_check = is_prime_num(factors[i])
        if prime_check is True:
            return factors[i]


factor_list = all_factors(num, empty)
prime_result = is_prime(factor_list)

if prime_result is True:
    print("That mother fucker is prime.")
    quit()
else:
    print("Tis not prime.  Here are the factors:")
    print(factor_list)


big_prime = largest_prime(factor_list)
print("One last trick, the largest prime factor is:")
print(big_prime)
