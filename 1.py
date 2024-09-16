"""1. Execute the given function.
def differenceofSum(n.m)

The function takes two integrals m and n as arguments.
You are required to obtain the total of all integers ranging between 1 to n
(both inclusive) which are not divisible by m.
You must also return the distinction between the sum of integers
not divisible by m with the sum of integers divisible by m.

Assumption
m > 0 and n > 0
Sum lies within the integral range
"""
def differenceofSum(n,m):
    notDivisible,Divisible=0,0
    for i in range(1,n+1):
        if i%m!=0:
            notDivisible+=i
        else:
            Divisible+=i
    distinction=notDivisible-Divisible
    return distinction
n,m=input("Enter two integrals: ").split()
n,m=int(n),int(m)
print("Distinction is: ",differenceofSum(n,m))
