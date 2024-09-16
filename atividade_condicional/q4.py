v = int(input("Informe um valor: "))

if v % 2==0:
    resultado=v+10
    (print(f"O valor {v} é par. Logo, {v} + 10 = {resultado}."))
else:
    resultado=v*10
    (print(f"O valor {v} é ímpar. Logo, {v} x 10 = {resultado}."))