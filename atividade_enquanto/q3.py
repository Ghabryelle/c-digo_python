import random 
num = 0

ne = random.randint(1, 100)
print("Adivinhe qual o número escolhido.")

tm = 5
t = 0

while t < tm:
    num = int(input(f"Digite o número {t + 1}: "))
    t += 1
    if num > ne: 
        print(f"O número {num} é maior que o número escolhido")
    elif num < ne:
        print(f"O número {num} é menor que o número escolhido")
    elif num == ne:
        print(f"Você acertou o número escolhido")
        
print(f"O número escolhido é {ne}.")