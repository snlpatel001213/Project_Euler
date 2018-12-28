# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def if_devisible(num):
    for i in range(1,20):
        if num%i != 0:
            return False
    return True

num = 1
while (num):
    if if_devisible(num):
        print(num)
        break
    num = num+1

# print(if_devisible(2520))