def es_primario(color):

    primarios=["rojo","amarillo","azul"]
    resultado=False
    for i in range(3):
        if color==primarios[i]:
            resultado = True
    return resultado

color= str(input("Ingrese el color: "))
if es_primario(color):
    print(f"El color es " + color + " primario")
else:
    print(f"El color " + color + " no es primario")
