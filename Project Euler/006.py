# Project Euler ex6:
# Sum Square difference
# Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum

def sum_of_squares():
    sum = 0
    for i in range(1, 101):
        sum += i**2
    print("The sum of all numbers squared: %d" % sum)
    return sum


def square_of_sum():
    sum = 0
    for i in range(1, 101):
        sum += i
    sum = sum**2
    print("All numbers summed up then squared: %d" % sum)
    return sum


sum_squares = sum_of_squares()
square_after = square_of_sum()
diff = square_after - sum_squares

print("The difference of the two is: %d" % diff)
