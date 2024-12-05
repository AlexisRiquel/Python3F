from tkinter import messagebox, Tk, StringVar, ttk

# Funciones del conversor

def convertir_temperatura():
    valor = entrada_temp.get()

    if not valor.isdigit():
        messagebox.showerror("Error","Por Favor, ingrese un valor numerico valido")
        return
    
    valor = float(valor)

#   Obtener las unidades seleccionadas usando .current()
    unidad_origen = unidad_origen_var.get()
    unidad_destino = unidad_destino_var.get()

    if unidad_origen == unidad_destino:
        resultado = valor
    elif unidad_origen == 'Celsius' and unidad_destino == 'Fahrenheit':
        resultado = (valor * 9/5) + 32
    elif unidad_origen == 'Celsius' and unidad_destino == 'Kelvin':
        resultado = valor + 273.15
    elif unidad_origen == 'Fahrenheit' and unidad_destino == 'Celsius':
        resultado = (valor - 32) * 5/9
    elif unidad_origen == 'Fahrenheit' and unidad_destino == 'Kelvin':
        resultado = (valor - 32) * 5/9 + 273.15
    elif unidad_origen == 'Kelvin' and unidad_destino == 'Celsius':
        resultado = valor - 273.15
    elif unidad_origen == 'Kelvin' and unidad_destino == 'Fahrenheit':
        resultado = (valor - 273.15) * 9/5 + 32

    # Mostrar el resultado
    etiqueta_resultado.config(text=f"Resultado: {resultado:.2f} {unidad_destino}")

# Ventana principal
root = Tk()

root.configure(background="#01e4ff")
root.title("Convertidor Temperatura")
root.geometry("400x300")
root.resizable(False,False)

# Centrar Ventana

window_width = 450
window_height = 270
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Colocando widgets a la interfaz

etiqueta_titulo = ttk.Label(root, text="Convertidor de Temperaturas", font=("Helvetica", 16))
etiqueta_titulo.grid(row=0, column=0, columnspan=5, pady=10)

etiqueta_temp = ttk.Label(root, text="Ingrese la temperatura:",font=(16))
etiqueta_temp.grid(row=1, column=0, padx=10, pady=5)

entrada_temp = ttk.Entry(root,font=(16))
entrada_temp.grid(row=1, column=1, padx=10,pady=5)

unidad_origen_var=StringVar()
unidad_origen_var.set("Celsius")

unidad_destino_var=StringVar()
unidad_destino_var.set("Fahrenheit")

etiqueta_origen = ttk.Label(root,text="Seleccionar unidad de origen:",font=(16))
etiqueta_origen.grid(row=2, column=0,padx=10, pady=5)

Combo_origen=ttk.Combobox(root,textvariable=unidad_origen_var)
Combo_origen["values"]=("Fahrenheit","Celsius","Kelvin")
Combo_origen.grid(row=2, column=1, padx=10, pady=5)

etiqueta_destino = ttk.Label(root,text="Seleccionar unidad de destino",font=(16))
etiqueta_destino.grid(row=3, column=0,padx=10, pady=5)

Combo_destino=ttk.Combobox(root,textvariable=unidad_destino_var)
Combo_destino["values"]=("Fahrenheit","Celsius","Kelvin")
Combo_destino.grid(row=3, column=1, padx=10, pady=5)

boton_convertir = ttk.Button(root,text="Convertir", command=convertir_temperatura)
boton_convertir.grid(row=4, column=0, columnspan=2, pady=20)

etiqueta_resultado=ttk.Label(root,text="Resultado",font=("Helvetica", 16))
etiqueta_resultado.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
