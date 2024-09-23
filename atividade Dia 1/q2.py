vlr = float(input("Valor pago: "))
pg = float(input("Digite o percentual de gorjeta: "))

print(f"Gorjeta: {vlr*(pg/100)}")
print(f"Total: {vlr+(vlr*(pg/100))}")