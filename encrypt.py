def pow_mod(n, pow, mod):
    binary_pow = bin(pow)[3:]
    result = n
    for i in binary_pow:
        result **= 2
        result %= mod
        if i == "1":
            result *= n
        result %= mod
    return result

print("== ENTER LOCK ==")
lock_num_1 = int(input("1st NUMBER : "))
lock_num_2 = int(input("2nd NUMBER : "))

txt = input("\nENTER MESSAGE: ")

print("\nENCRYPTED MESSAGE: ")
encrypted_num = []
for i in txt:
    encrypted_num.append(str(pow_mod(ord(i),lock_num_1,lock_num_2)))

print(",".join(encrypted_num))
    
input()