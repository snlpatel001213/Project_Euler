# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.\
from tqdm import tqdm

def if_pallindrome(number):
    original_num = number
    reverse_num = 0
    while(number > 0):
        num = number % 10
        reverse_num = reverse_num * 10 + num
        number = number//10
    if original_num == reverse_num:
        return True
    else:
        return False

for i in tqdm(range(999,100,-1)):
    for j in range(999, 100, -1):
        product = i*j
        if if_pallindrome(product) == True:
            print (i,j,product)
            break

print(if_pallindrome(12321))
