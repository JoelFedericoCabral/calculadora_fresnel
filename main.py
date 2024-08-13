import tkinter as tk
from tkinter import ttk

def calcular_fresnel():
    try:
        distancia = float(entry_distancia.get())
        frecuencia = float(entry_frecuencia.get())
        fresnel_metros = 8.656 * ((distancia / frecuencia) ** 0.5)
        unidad = unidad_var.get()

        if unidad == "Pies":
            resultado = fresnel_metros * 3.28084
        elif unidad == "Kilómetros":
            resultado = fresnel_metros / 1000
        else:  # Metros
            resultado = fresnel_metros

        etiqueta_resultado.config(text=f"Zona de Fresnel: {resultado:.2f} {unidad.lower()}", foreground="#4CAF50")
    
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingrese valores numéricos válidos.", foreground="red")

# Configuracion de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de la Zona de Fresnel")
ventana.geometry("450x300")
ventana.resizable(False, False)

# Fondo degradado
background_gradient = tk.Canvas(ventana, width=450, height=300)
background_gradient.place(x=0, y=0)
for i in range(300):
    r = int(255 - (i/300)*100)
    g = int(255 - (i/300)*50)
    b = int(255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    background_gradient.create_line(0, i, 450, i, fill=color)

# Estilos
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
style.configure("TButton", font=("Arial", 12, "bold"), background="#4CAF50", foreground="white", borderwidth=0, padding=6)
style.map("TButton", background=[('active', '#45a049')])
style.configure("TEntry", font=("Arial", 12))

# Creacion y ubicacion de las etiquetas y cuadros de entrada con un marco estilizado
frame = ttk.Frame(ventana, padding="20 10 20 10", style="TFrame")
frame.place(relx=0.5, rely=0.5, anchor="center")

ttk.Label(frame, text="Distancia (km):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_distancia = ttk.Entry(frame)
entry_distancia.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(frame, text="Frecuencia (GHz):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_frecuencia = ttk.Entry(frame)
entry_frecuencia.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Creacion y ubicacion  del menú desplegable para seleccionar la unidad
ttk.Label(frame, text="Unidad de resultado:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
unidad_var = tk.StringVar(value="Metros")
menu_unidades = ttk.Combobox(frame, textvariable=unidad_var, values=["Metros", "Pies", "Kilómetros"])
menu_unidades.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Creacion y ubicacion del botón para calcular
boton_calcular = ttk.Button(frame, text="Calcular", command=calcular_fresnel)
boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Creacion y ubicacion de la etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(frame, text="Zona de Fresnel:", font=("Arial", 12, "bold"))
etiqueta_resultado.grid(row=4, column=0, columnspan=2, pady=10)

# Ajuste de columnas
frame.grid_columnconfigure(1, weight=1)

# Footer con el nombre
footer_label = ttk.Label(ventana, text="Creado por Joel Cabral", font=("Arial", 10))
footer_label.pack(side="bottom", pady=5)

# Ejecuta el bucle principal de la interfaz
ventana.mainloop()
