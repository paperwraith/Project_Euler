# find the first number that is divisble by every number 1 to 20

def loop():
    num = 2520
    divisor = 2

    while divisor < 21:
        if num % divisor == 0:
            divisor += 1
        else:
            num += 1
            divisor = 2
    print(num)


loop()
