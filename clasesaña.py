class Producto():
    def __init__(self, nombre, precio_base, stock):
        self.nombre = nombre
        self.precio_bs = precio_base
        self.stock = stock

    def Aplicardescuento (self, porcentaje):
        self.precio_bs*=(1-porcentaje)
        print (f"El nuevo precio del producto es {self.preciobs}")

    def actualizar_stock(self, cantidad):
        if (self.stock+cantidad)<0:
            print("no hay suficiente stock") 
        else:
            self.stock+=cantidad   
            print(f"El nuevo stock de {self.nombre} es {self.stock}")

