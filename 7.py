# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def is_prime(test_num):
    if test_num % 2 ==0:
        return False
    for i in range(3, test_num,2):
        if test_num%i == 0:
            return False
    return True

num  = 1
counter  = 0
while (num):
    if is_prime(num) == True:
        counter+=1
    elif counter == 10001:
        print (counter,num-1)
        break
    num +=1