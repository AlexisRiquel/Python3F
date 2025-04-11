def dividir_numeros():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")


dividir_numeros()

