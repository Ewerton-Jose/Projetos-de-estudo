# Tabelas verdades

p = [True, True, True, True, False, False, False, False]
q = [True, True, False, False, True, True, False, False]
v = [True, False, True, False, True, False, True, False]


# Perguntando as infromações das preposições com tratamento de erro

while True:
    try:
        quant_preposicoes = int(input("Digite os numeros de preposiçẽos que você quer [Valor máximo 3]: "))
    except:
        print("Coloque um valor inteiro")
    else:
        if (quant_preposicoes > 3) or (quant_preposicoes < 0):
            print("Maior que 3 ou menor que 0")
            pass
        else: break

# Verificando a quantidade de V e F

quant_VF = 2 ** quant_preposicoes


if quant_VF == 4:
    for c in range(4):
        print(p[c + 2],  q[c + 1])

if quant_VF == 8:
    for c in range(7):
        print(p[c],  q[c], v[c])