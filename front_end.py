import tkinter as tk
from back_end import *
from tkinter import messagebox

def ventana_principal():
    vent1=tk.Tk()
    vent1.title("Base de datos")
    vent1.geometry("600x650")


    etiq1=tk.Label(vent1, text="Nombre")
    etiq1.pack()
    entrada1=tk.Entry(vent1, width=60)
    entrada1.pack(pady=10)

    etiq2=tk.Label(vent1, text="Edad")
    etiq2.pack()
    entrada2=tk.Entry(vent1, width=60)
    entrada2.pack(pady=10)

    etiq3=tk.Label(vent1, text="Contraseña")
    etiq3.pack()
    entrada3=tk.Entry(vent1, width=60)
    entrada3.pack(pady=10)

    def registrar():
        name=entrada1.get()
        age=entrada2.get()
        food=entrada3.get()
        newuser=Usuario(name, age, food)
        entrada1.delete(0,tk.END)
        entrada2.delete(0,tk.END)
        entrada3.delete(0,tk.END)
        messagebox.showinfo("Registro de usuario", "Tu registro fue exitoso")

    boton1=tk.Button(vent1,text="Registrar",command=registrar)
    boton1.pack(pady=20)
    def mostrar_lista():
        Usuario.mostrar_lista()

    boton2=tk.Button(vent1,text="Mostrar lista",command=mostrar_lista)
    boton2.pack(pady=20)

    def al_cerrar():
        print("Guardando datos antes de salir...")
        Usuario.guardar_usuarios()
        vent1.destroy()
        

    vent1.protocol("WM_DELETE_WINDOW", al_cerrar)
    vent1.mainloop()
ventana_principal()
def ventana_login():
    ven2=tk.Tk()
    ven2.title("Inicio de sesion")
    ven2.geometry("400x300")
    Usuario.cargar_usuarios()
    etiqueta3=tk.Label(ven2,text="Usuario")
    etiqueta3.pack()
    entrada4=tk.Entry(ven2,width=60)
    entrada4.pack(pady=10)
    etiqueta4=tk.Label(ven2,text="Password")
    etiqueta4.pack(pady=10)
    entrada5=tk.Entry(ven2,width=60)
    entrada5.pack(pady=10)
    def iniciar():
        name=entrada4.get()
        password=entrada5.get()
        for x in Usuario.lista:
            if name == x.nombre:
                if password==x.contra:
                    ventana_principal()
            else:
                messagebox.showwarning("inicio de sesión", "El usuario no existe")
    boton4=tk.Button(ven2,text="iniciar sesion", command=iniciar)
    boton4.pack(pady=10)
    ven2.mainloop()