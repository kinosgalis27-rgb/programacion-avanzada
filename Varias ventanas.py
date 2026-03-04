import tkinter as tk
from PIL import Image, ImageTk 

def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Esta es mi ventana principal")
    ven1.geometry("600x300")
    ven1.config(bg="lightblue")

    eti1=tk.Label(ven1,text="Reino Animal",bg="lightblue",font=("Arial",23,"bold"))
    eti1.pack()
    frame1= tk.Frame(ven1)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open(r"C:\Users\Salon202\Kino progra\ReinoAnimal.jpg")
    imagen = imagen.resize((400, 200))  
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    frame2=tk.Frame(frame1)
    frame2.grid(row=0, column=1, padx=5, pady=5)
    var=tk.IntVar()
    ele=tk.Radiobutton(frame2,text="Elefante",variable=var,value=1)
    ele.pack()
    jirafa=tk.Radiobutton(frame2,text="Jirafa",variable=var,value=2)
    jirafa.pack()
    castor=tk.Radiobutton(frame2,text="Castor",variable=var,value=3)
    castor.pack()
    leon=tk.Radiobutton(frame2,text="León",variable=var,value=4)
    leon.pack()

def informacion():
    seleccion = var.get()
    if seleccion == 1:
        ventana_elefante()
    elif seleccion == 2:
        ventana_jirafa()

    boton1=tk.Button(ven1,text="Ver info",command=informacion)
    boton1.pack()

    ven1.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy() 
    ventana_principal() 

def ventana_elefante():
    global ven2
    ven1.destroy()

    ven2 = tk.Tk()
    ven2.title("Información del elefante")
    ven2.geometry("500x500")
    ven2.config(bg="gray")

    eti2 = tk.Label(ven2, text="Elefante", bg="gray",
                    font=("Algerian", 24, "bold"))
    eti2.pack(pady=10)

    frame3 = tk.Frame(ven2)
    frame3.pack(pady=20)

    imagen2 = Image.open(r"C:\Users\Salon202\Kino progra\52dp251ljx_Medium_WW2122503.jpg")
    imagen2 = imagen2.resize((200, 200))
    imagen_tk2 = ImageTk.PhotoImage(imagen2)
    label_imagen = tk.Label(frame3, image=imagen_tk2)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    label_imagen.image = imagen_tk2

    etiqueta2 = tk.Label(
        frame3,
        text="Los elefantes o elefántidos son una familia de mamíferos "
             "placentarios del orden proboscídeos. Existen hoy en día "
             "tres especies y diversas subespecies.",
        wraplength=200,
        justify="left"
    )
    etiqueta2.grid(row=0, column=1, padx=5, pady=5)

    boton2 = tk.Button(
        ven2,
        text="Ir a ventana principal",
        command=lambda: regresar_a_primera(ven2)
    )
    boton2.pack(pady=30)
    ven2.mainloop()

def ventana_jirafa():
    global ven2
    ven1.destroy()

    ven2 = tk.Tk()
    ven2.title("Información de la jirafa")
    ven2.geometry("500x500")
    ven2.config(bg="beige")

    titulo = tk.Label(ven2, text="Jirafa",
                      bg="beige",
                      font=("Algerian", 24, "bold"))
    titulo.pack(pady=10)

    frame3 = tk.Frame(ven2, bg="beige")
    frame3.pack(pady=20)

    
    imagen2 = Image.open(r"C:\Users\Salon202\Kino progra\Giraffa_camelopardalis_angolensis.jpg")
    imagen2 = imagen2.resize((400, 250))

    imagen_tk2 = ImageTk.PhotoImage(imagen2)

    label_imagen = tk.Label(frame3, image=imagen_tk2, bg="beige")
    label_imagen.grid(row=0, column=0, padx=5)

    label_imagen.image = imagen_tk2

    texto = tk.Label(
        frame3,
        text="La jirafa es el animal terrestre más alto del mundo. "
             "Habita principalmente en África y se caracteriza por su cuello largo.",
        wraplength=200,
        justify="left",
        bg="beige"
    )
    texto.grid(row=0, column=1, padx=5)

    boton = tk.Button(
        ven2,
        text="Ir a ventana principal",
        command=lambda: regresar_a_primera(ven2)
    )
    boton.pack(pady=30)

    ven2.mainloop()

ventana_principal()