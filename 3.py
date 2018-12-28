# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
from tqdm import tqdm
import math
lower = 1
upper = 600851475143

def is_prime(test_num):
    if test_num % 2 ==0:
        return False
    for i in range(3, test_num,2):
        if test_num%i == 0:
            return False
    return True

for num in tqdm(range (int(math.sqrt(upper-1)), lower,-1)):
    # print(num)
    if (upper%num==0):
        if (is_prime(num)):
            print(num)
            break
