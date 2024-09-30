numero = int(input("Introduzca un numero entre 1 y 20: "))

for i in range(numero // 2):
    for j in range(numero - 2):
        print(" ", end="")
    print("***")

for i in range(numero, 0, -1):
    for j in range(numero - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


