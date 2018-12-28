# Special Pythagorean triplet
import math
import numbers

def find_valid_pythagoras(num1, num2):
    c =  num1**2+ num2**2
    diffence =  int(math.sqrt(c)) - math.sqrt(c)
    if diffence == 0:
        return True, int(math.sqrt(c))
    else:
        return False, int(math.sqrt(c))

for a in range (0,1001):
    for b in range(0, 1001):
        if a < b:
            bool_ , c = find_valid_pythagoras(a,b)
            if bool_ == True :
                if int(a+b+c) == 1000:
                    print (a*b*c, a,b,c)
                    break
