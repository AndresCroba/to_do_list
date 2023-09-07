import tkinter as tk

# Función para agregar una tarea
def agregar_tarea():
    tarea = entrada.get()
    
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)

# Función para eliminar una tarea seleccionada
def eliminar_tarea():
    tarea_seleccionada = lista_tareas.curselection()
    
    if tarea_seleccionada:
        lista_tareas.delete(tarea_seleccionada)


# Crear una ventana
ventana = tk.Tk()
ventana.title("To-Do List")

# Crear una entrada para agregar tareas
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Botones para agregar y eliminar tareas
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_agregar.pack()
boton_eliminar.pack()


# Lista de tareas
lista_tareas = tk.Listbox(ventana, selectmode=tk.SINGLE)
lista_tareas.pack()


# Ejecutar la ventana
ventana.mainloop()