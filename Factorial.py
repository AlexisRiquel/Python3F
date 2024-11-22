def calcular_factorial(n):
    if n < 0:
        print("El numero debe ser entero positivo")
    else:
      
        factorial = 1

        for i in range(1, n + 1):
            factorial *= i

        print(f"El factorial de {n} es: {factorial}") 

numero = int(input("Ingresa un numero entero positivo: "))
calcular_factorial(numero)
