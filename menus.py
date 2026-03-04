import tkinter as tk
from tkinter import messagebox

def nuevo_archivo():
    messagebox.showinfo("Informacion", "Creaste un nuevo archivo")
def abrir_archivo():
    messagebox.showinfo("Informacion", "Abriste un archivo")
def guardar_archivo():
    messagebox.showinfo("Informacion", "guardaste un nuevo archivo")
def cortar_archivo():
    messagebox.showinfo("Informacion", "cortaste un texto")
def pegar_archivo():
    messagebox.showinfo("Informacion", "pegaste un texto")
    
ven1=tk.Tk()
ven1.title("Uso de menus")
ven1.geometry("500x400")

barra_menu=tk.Menu(ven1)

menu_archivo=tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)

menu_edicion=tk.Menu(barra_menu, tearoff=0)
menu_edicion.add_command(label="Cortar", command=cortar_archivo)
menu_edicion.add_command(label="pegar", command=pegar_archivo)

barra_menu.add_cascade(label="Archivo",menu=menu_archivo)
barra_menu.add_cascade(label="edicion",menu=menu_edicion)
ven1.config(menu=barra_menu)

ven1.mainloop()