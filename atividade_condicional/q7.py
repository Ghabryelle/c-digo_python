v = float(input("Informe o valor: "))
m = int(input("Informe o metodo de pagamento:\n 1-Pix,dinheiro ou débito, recebe 15% de desconto \n 2-Pix,dinheiro ou débito, recebe 15% de desconto\n 3-Em duas vezes, preço normal sem juros\n 4-Em três vezes, preço normal mais juros de 10% "))

if m==1:
    desconto= v*0.15
    final= v-desconto
    (print(f"Valor a ser pago é de R$ {final:.2f}."))

elif m== 2:
    desconto = v*0.10
    final=v-desconto
    (print(f"Valor a ser pago é de R$ {final:.2f}."))

elif m==3:
    print(f"Valor a ser pago é de R$ {v:.2f}.")
    
elif m==4:
    desconto= v*0.10
    final= v+desconto
    print(f"Valor a ser pago é de R$ {final :.2f}.")
    
else:
    (print("Método de pagamento não selecionado!"))
    
