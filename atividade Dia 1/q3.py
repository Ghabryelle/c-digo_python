import time 

seg = int(input("Digite os segundos: "))

for contador in range(seg, -1, -1):
    print(contador)
    time.sleep(1)
print("Tempo esgotado!")