import csv
import os
class Usuario():
    lista=[]
    ruta_csv=r"C:/Users/Salon202/Kino.csv"
    def __init__ (self, name,age,contr):
        self.nombre=name
        self.edad=age
        self.contra=contr
        if self not in Usuario.lista:
            Usuario.lista.append(self)

    def mostrar_datos(self):
        return f"El usuario {self.nombre} tiene {self.edad} años y su password es {self.contra}"

    @classmethod #metodo de clase
    def mostrar_lista(cls):
        for u in Usuario.lista:
            print (u.mostrar_datos())

    @classmethod
    def guardar_usuarios(cls):
        campos=["nombre", "edad","contraseña"]#nombres de la columna de la tabla

        #crear el directorio
        directorio= os.path.dirname(cls.ruta_csv)
        if not os.path.exists(directorio):
            try:
                os.makedirs(directorio)
                print(f"directorio creado {directorio}")
            except Exception as e:
                print(f"error al crear directorio: {e}")
                return False

            #guardar el archivo
        with open(cls.ruta_csv, "w", newline='',encoding="utf-8") as f:
            escritor=csv.DictWriter(f, fieldnames=campos, delimiter=',')
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow({"nombre":u.nombre,"edad":u.edad,"contraseña":u.contra})
                
    @classmethod
    def cargar_usuarios(cls):
         if not os.path.exists(cls.ruta_cvs):
            print("No hay base de datos previa")
            return
            
         with open(cls.ruta_csv, "r", encoding="utf-8") as f:
             lector = csv.DictReader(f)
             cls = []
             for fila in lector:
                 Usuario(fila["nombre"], fila["edad"], fila["contraseña"])
         print("Datos cargados exitosamente")