#SHELDON COOPER'S BEST NUMBER(which is 73) :P
import math  #IMPORTING MATH FUNCTION
def isPrime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True    
n=int(input())  #GETTING RANGE FROM USER(to check any other number like that)
primes_pos = []
for i in range(2,n):
    if(isPrime(i)):
        primes_pos.append(i)
for i in range(12,n):
    string=str(i)
    string_mod=string[::-1]
    string_2=int(string_mod)
    if(i in primes_pos and string_2 in primes_pos):
        a=primes_pos.index(i)+1
        b=primes_pos.index(string_2)+1
        a_rev=str(a)[::-1]
        b_rev=str(b)
        if a_rev == b_rev:
            print(i)
