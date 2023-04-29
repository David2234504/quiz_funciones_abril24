print("------------------------------------")
print("-------Curiosidad matematica--------")
print("------------------------------------")

def suma_impares(n):
    suma = 0
    for i in range(1, n*2, 2):
        suma += i
    return suma

def verifica_curiosidad(n):
    cuadrado_n = n**2
    suma = suma_impares(n)
    if cuadrado_n == suma:
        print(f"La curiosidad matemática es VERDADERA para n = {n}")
    else:
        print(f"La curiosidad matemática es FALSA para n = {n}")

n = int(input("Ingrese un número entero positivo: "))
verifica_curiosidad(n)
