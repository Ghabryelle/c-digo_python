n = (input("Informe seu nome: "))
s = (input("Informe seu sexo: "))
e = (input("Informe seu estado civil: "))


if s=="F" and e=="casada":
    c = (input("Informe há quantos anos você é casada: \n"))
    print(f"{n}, casada há {c} anos.")
else:
     print(f"{n}, obrigado. Até a próxima!")