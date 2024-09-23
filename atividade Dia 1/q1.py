atv = (input("Você praticou caminhada, corrida ou ciclismo: "))
minu = int(input("Quantos minutos: "))


if atv == "caminhada":
    print(f"Você perdeu {5 * minu} calorias")
    
if atv == "corrida":
    print(f"Você perdeu {10 * minu} calorias")
    
if atv == "ciclismo": 
    print(f"Você perdeu {8 * minu} calorias")
    