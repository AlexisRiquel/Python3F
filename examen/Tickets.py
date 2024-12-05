import pickle
import random
import sys
import os

# Archivo donde se guardarán los tickets
TICKET_FILE = 'tickets.pkl'

# Función para generar un nuevo ticket con un número aleatorio
def generar_ticket_id():
    return random.randint(1000, 9999)

# Función para cargar los tickets desde el archivo
def cargar_tickets():
    if os.path.exists(TICKET_FILE):
        
        with open(TICKET_FILE, 'rb') as f:
            try:
                tickets = pickle.load(f)
            except EOFError:
                tickets = []
    else:
        tickets = []
    return tickets

# Función para guardar los tickets en el archivo
def guardar_tickets(tickets):
    with open(TICKET_FILE, 'wb') as f:
        pickle.dump(tickets, f)

# Función para crear un nuevo ticket
def alta_ticket():
    while True:

        nombre = input("Ingrese el nombre del usuario: ")
        sector = input("Ingrese el sector: ")
        asunto = input("Ingrese el asunto: ")
        problema = input("Describa el problema: ")

        ticket_id = generar_ticket_id()
        ticket = {
            'id': ticket_id,
            'nombre': nombre,
            'sector': sector,
            'asunto': asunto,
            'problema': problema
        }

        # Guardamos el ticket
        tickets = cargar_tickets()
        tickets.append(ticket)
        guardar_tickets(tickets)

        # Mostrar el ticket y el número
        print("\n--- TICKET CREADO ---")
        print(f"ID: {ticket['id']}")
        print(f"Nombre: {ticket['nombre']}")
        print(f"Sector: {ticket['sector']}")
        print(f"Asunto: {ticket['asunto']}")
        print(f"Problema: {ticket['problema']}")
        print("\nRecuerde el número del ticket para consultas futuras.")

        # Preguntar si desea crear otro ticket
        crear_otro = input("\n¿Desea crear otro ticket? (s/n): ")
        if crear_otro.lower() == 'n':
            break 
        elif crear_otro.lower() != 's':
            print("Se ingreso una opcion no valida, se regresa al menu principal")
            break

# Función para leer un ticket por número
def leer_ticket():
    while True: 
        ticket_id = int(input("\nIngrese el número de ticket para leer: "))
        tickets = cargar_tickets()

        encontrado = False
        for ticket in tickets:
            if ticket['id'] == ticket_id:
                print("\n--- TICKET ENCONTRADO ---")
                print(f"ID: {ticket['id']}")
                print(f"Nombre: {ticket['nombre']}")
                print(f"Sector: {ticket['sector']}")
                print(f"Asunto: {ticket['asunto']}")
                print(f"Problema: {ticket['problema']}")
                encontrado = True
                break

        if not encontrado:
            print("Ticket no encontrado.")

        # Preguntar si desea leer otro ticket
        leer_otro = input("\n¿Desea leer otro ticket? (s/n): ")
        if leer_otro.lower() == 'n':
            break 
        elif leer_otro.lower() != 's':
            print("Se ingreso una opcion no valida, se regresa al menu principal")
            break

# Función para mostrar el menú principal
def mostrar_menu():
    while True:
        print("\n--- Menú de Gestión de Tickets ---")
        print("1. Alta de ticket")
        print("2. Leer ticket")
        print("3. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                alta_ticket()
            elif opcion == 2:
                leer_ticket()
            elif opcion == 3:
                salir = input("\n¿Está seguro que desea salir? (s/n): ")
                if salir.lower() == 's':
                    print("Saliendo del programa...")
                    sys.exit(0)
                else:
                    continue
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == '__main__':
    mostrar_menu()
