from math import sqrt as sq
def check(n):
    if n==2 or n==3 or n==4:
        return True
    if n%2==0:
        return False
    for i in  range(2,int(sq(n)+1),2):
        if n%i==0:
            return False
    
    return True

#Main code
print("Enter the number")
n = int(input())
if n==1:
    print("1 is neither prime nor composite")
elif check(n):
    print("It is a prime number")
else:
    print("It is not a prime number")