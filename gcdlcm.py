def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

#Main code
a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
lcm = a*b
lcm//=gcd(a,b)
print("GCD of a and b is",gcd(a,b),"and LCM of a and b is",lcm)