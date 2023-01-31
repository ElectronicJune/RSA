import math
import random

print("== ENTER 2 DIFFERENT LARGE PRIME NUMBERS ==")
p = int(input("1st PRIME: "))
q = int(input("2nd PRIME: "))

if p == q :
    print("\n!!! Primes can't be same.")
    input()
    exit()

n = p * q

if n < 128 :
    print("\n!!! Prime numbers too small.")
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

print()
print(f"lock : {e}, {n}")
print(f"key  : {d}, {n}")

input()
        
            




