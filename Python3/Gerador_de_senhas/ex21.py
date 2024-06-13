import random

algarismos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%*()_"

total_algarismos  = len(algarismos) -1

quantidade_digitos_maximos = random.randint(8, total_algarismos)

senha = ""

count = 0
while True:
    senha += algarismos[random.randint(0, total_algarismos)]
    count = count + 1
    if count == quantidade_digitos_maximos: break


print(f"Your new key is:\033[;1m \033[0;32m {senha}")