def abrir_o_crear_archivo():
    nombre_archivo = "documento.txt"

    try:
        
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print("Archivo encontrado. Contenido:")
            print(contenido)
    except FileNotFoundError:
       
        print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
        print("Creando un nuevo archivo...")
        
        
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Este es el contenido inicial del archivo creado.\n")
        
        print(f"El archivo '{nombre_archivo}' ha sido creado exitosamente.")


abrir_o_crear_archivo()
