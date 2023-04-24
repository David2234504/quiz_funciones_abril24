print("----------------------------------------")
print("----------Tabla de multiplicar----------")
print("----------------------------------------")

#funcion
def generartabla(numero):
    print("Tabla del", numero)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{i} x {numero} = {resultado}")

numero = int(input("Digite el número: "))
generartabla(numero)
