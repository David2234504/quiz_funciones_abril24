print("------------------------------------")
print("---------Ultimo digito es 4---------")
print("------------------------------------")

def verificar_numero_4(n):
    if n % 10 == 4:
        print("Su ultimo digito es 4.")
    else:
        print("Su ultimo digito no es 4.")

n = int(input("Digite el número: "))
verificar_numero_4(n)