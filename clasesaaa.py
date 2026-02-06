class Producto():
    def __init__(self, nombre, precio_base, stock):
        self.nombre = nombre
        self.precio_bs = precio_base
        self.stock = stock

    def Aplicardescuento(self, porcentaje):
        self.precio_bs *= (1 - porcentaje)
        print(f"El nuevo precio del producto es {self.precio_bs}")

    def actualizar_stock(self, cantidad):
        if (self.stock + cantidad) < 0:
            print("no hay suficiente stock") 
        else:
            self.stock += cantidad   
            print(f"El nuevo stock de {self.nombre} es {self.stock}")


class Categoria():
    def __init__(self, nombre_categoria):
        self.nomcat = nombre_categoria
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print(f"El producto {producto.nombre} se agregó a la lista")

    def valor_total_categoria(self):
        suma = 0
        for m in self.lista_productos:
            suma += m.precio_bs * m.stock
        print(f"El precio total de la categoria {self.nomcat} es {suma} pesos")

class Pedido
