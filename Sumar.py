def sumar_valores():
    num = int(input("Ingresa un número: "))
    texto = input("Ingresa una palabra: ")

    try:
        resultado = num + texto
        print(f"Resultado: {resultado}")
    except TypeError:
        print("Error: No se puede sumar un número y una cadena.")


sumar_valores()
