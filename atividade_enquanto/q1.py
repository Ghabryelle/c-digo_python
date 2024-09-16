valor = 0

while valor >= 0:
    
    valor = int(input("Digite um valor: "))

    if valor > 10 and valor <= 100: 
        print(f"O dobro de {valor} é {valor*valor}")
    
    if valor > 5 and valor < 10: 
        print(f"O cubo de {valor} é {valor*valor*valor}")
    
    if valor > 100: 
        print("Limite Excedido")