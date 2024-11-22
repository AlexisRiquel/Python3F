def calcular_mayor():
    n = int(input("¿Cuántos numeros deseas ingresar? "))
    resultado=0
    for i in range(n):
        numero = int(input(f"Ingrese el numero {i+1}: "))
        if numero > resultado:
            resultado=numero
    return resultado

mayor = calcular_mayor()
print(f"El mayor es: {mayor}")
