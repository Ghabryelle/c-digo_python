a = int(input("Qual o valor A: "))
b = int(input("Qual o valor B: "))
c = int(input("Qual o valor C: "))

if a>b>c:
    (print(f"{c},{b} e {a}"))
if a>c>b:
    (print(f"{b},{c} e {a}"))
if b>c>a:
    (print(f"{a},{c} e {b}"))
if b>a>c:
    (print(f"{c},{a} e {b}"))
if c>a>b:
    (print(f"{b},{a} e {c}"))
if c>b>a:
    (print(f"{a},{b} e {c}"))