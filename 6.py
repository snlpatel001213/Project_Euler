# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math
def find_sum_of_square(num):
    sum_of_squre = 0
    for i in range(num+1):
        sum_of_squre += i**2
    return sum_of_squre

def find_square_of_sum(num):
    sum_of_squre = 0
    for i in range(num+1):
        sum_of_squre += i
    print(sum_of_squre)
    return sum_of_squre**2

print(find_square_of_sum(100) - find_sum_of_square(100) )