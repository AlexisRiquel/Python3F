def dibujar_rectangulo():
    filas = int(input("Ingresar el numero de filas: "))
    columnas = int(input("Ingresar el numero de columnas: "))
    if numeros_iguales(filas,columnas):
        print("No se pueden ingresar numeros iguales")
    else:
        for i in range(filas):
            print('x' * columnas)

def numeros_iguales(filas,columnas):
    return filas==columnas

dibujar_rectangulo()
