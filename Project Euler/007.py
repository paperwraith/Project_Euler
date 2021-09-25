# Project Euler ex7
# 10001st Prime
# Find the 10,001st prime number


# divides a number by every number less than itself.  stops if found a factor.
def prime_identify(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


# finds the nth prime
def all_primes(target):
    iteration = 2
    prime = 0
    count = 0

    while count < target:
        iteration += 1
        checker = prime_identify(iteration)

        if checker is True:
            prime = iteration
            count += 1
    return prime


print(all_primes(10001))
