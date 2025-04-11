def buscar_clave():
    persona = {
        "nombre": "Luis",
        "edad": 25,
        "ciudad": "Madrid"
    }

    clave = input("Ingresa la clave que deseas buscar: ")

    try:
        valor = persona[clave]
        print(f"El valor de '{clave}' es: {valor}")
    except KeyError:
        print(f"Error: La clave '{clave}' no existe en el diccionario.")


buscar_clave()
