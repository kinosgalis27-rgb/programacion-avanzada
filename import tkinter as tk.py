import tkinter as tk
from PIL import Image, ImageTk

def actualizar_etiqueta():
    nuevo_texto= entrada.get()
    etiqueta.config(text=nuevo_texto)
ventana1 = tk.Tk()
ventana1.title("Ejemplo basico")
ventana1.geometry("1000x1000")

entrada = tk.Entry(ventana1, width=60)
entrada.pack(pady=10)

boton=tk.Button(ventana1, text="actulizar", command=actualizar_etiqueta)
boton.pack()

etiqueta = tk.Label(ventana1, text="txto inicial", font= ("Arial", 12))
etiqueta.pack(pady=10)

def boton_clic():
    print("hiciste click")

boton = tk.Button(ventana1, text="haz clic aquí", command=boton_clic,
                font=("comic sans", 30))
boton.pack(pady=20)
imagen= Image.open("images (1).jpeg")
imagen = imagen.resize((300, 400))
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana1, image=imagen_tk)
label_imagen.pack(pady=20)


etiqueta = tk.Label(ventana1, text= "Aña, grupo de progra avanzada",
    font= ("Arial", 14, "bold"), fg="black", bg="yellow", padx= 20, pady=10)
etiqueta.pack()
etiqueta2 = tk.Label(ventana1, text= "Mi nombre es Bernardo joaquín",
    font= ("Arial", 20, "bold"), padx= 20, pady=10)
etiqueta2.pack()
etiqueta3 = tk.Label(ventana1, text= "Estudio Ing en Ciencias de la computación",
    font= ("Arial", 20, "bold"), padx= 20, pady=10)
etiqueta3.pack()
etiqueta4 = tk.Label(ventana1, text= "Me gusta Merari",
    font= ("Arial", 20, "bold"), fg="black", bg="red", padx= 20, pady=10)
etiqueta4.pack()
ventana1.mainloop()
