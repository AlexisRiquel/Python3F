def calcular_promedio():
    # Solicitar al usuario el número de notas
    n = int(input("¿Cuántas notas deseas ingresar? "))
    
    # Crear una lista para almacenar las notas
    notas = []
    
    # Solicitar las notas al usuario
    for i in range(n):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    
    # Calcular el promedio
    promedio = sum(notas) / n
    
    return promedio

# Llamar a la función y mostrar el resultado
promedio = calcular_promedio()
print(f"El promedio de las notas es: {promedio}")
