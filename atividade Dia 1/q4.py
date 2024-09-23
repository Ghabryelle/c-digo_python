import random 

print("Bem-vindo ao Jogo com o robôzinho :) \n")

res = (input("Você deseja jogar? "))

while res == "sim":
    print("\nPedra = 1 \nPapel = 2 \nTesoura = 3\n")
    ppt = random.randint(1, 3)
    ne = int(input("Escolha um número entre 1 e 3: "))
    print(f"\nO robôzinho escolheu o número {ppt}.")

    if ppt == 1 and ne == 3:
        print("Pedra ganha de Tesoura.")
    
    if ppt == 1 and ne == 2:
        print("Papel ganha de Pedra.")
    
    if ppt == 1 and ne == 1:
        print("Os dois escolheram Pedra.")
    
    if ppt == 2 and ne == 3:
        print("Tesoura ganha de Papel.")
    
    if ppt == 2 and ne == 2:
        print("Os dois escolheram Papel.")
    
    if ppt == 3 and ne == 3:
        print("Os dois escolheram Tesoura.")
    
    res = (input("\nVocê deseja jogar novamente? "))
    if res == "não": 
        print("\nObrigada por brincar comigo! <3")