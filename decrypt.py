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

print("== ENTER KEY ==")
key_num_1 = int(input("1st NUMBER : "))
key_num_2 = int(input("2nd NUMBER : "))

decrypted_list = input("\nENTER LIST : ").split(",")

print("\nMESSAGE: ")
for i in decrypted_list:
    print(chr(pow_mod(int(i),key_num_1,key_num_2)),end="")

input()


    
