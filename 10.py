# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from tqdm import tqdm
from multiprocessing import Pool
import numpy

def is_prime(test_num):
    if test_num % 2 ==0 and test_num!=2:
        return None
    for i in range(3, test_num,2):
        if test_num%i == 0:
            return None
    return test_num

sum = 0
p2 = Pool()
r2 = p2.map(is_prime,numpy.arange(2,2000000))
print(r2)
for i in r2:
    if i != None:
        sum = sum + i

print(sum)
