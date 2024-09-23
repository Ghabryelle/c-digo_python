num = []

while True:
    valor = int(input("Digite um valor: "))
    if valor < 0:
        break
    else:
        num.append(valor)
print(num)

for contador in num:
    if contador % 2 == 0:
        num.remove(contador)
print(num)    
    