import math
import random

print("==give 2 different large prime numbers==")
p = int(input("prime 1: "))
q = int(input("prime 2: "))

if p == q :
    print("primes can not be the same.")
    input()
    exit()

n = p * q

if n < 128 :
    print("prime numbers not large enough.")
    input()
    exit()

pn = (p-1) * (q-1)

e_list = []
for i in range(3,pn):
    if math.gcd(i, pn) == 1 :
        e_list.append(i)

e = e_list[random.randrange(0,len(e_list))]

d_index = random.randrange(1, 100)

d = 1
for i in range(0, d_index + 1):
    while d * e % pn != 1:
        d += 1
    if i == d_index:
        break
    
print(f"lock : {e}, {n}")
print(f"key  : {d}, {n}")

input()
        
            




