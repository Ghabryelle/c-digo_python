meses = [" ","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
tm = 12
t = 0
mA = 0

while t < tm:
    temp = int(input(f"Temperatura média de {meses[t + 1]}: "))
    t += 1
    
    mA += temp
print(f"Média anual: {mA/12:.2f} ºC")