class usuario:
    def __init__(self, id_usuario, nombre, punto):
        self.id_usuario =id_usuario
        self.nom=nombre
        self.pto=punto
        
    def ver_informacion(self):
        return f"El usuario {self.nom} tiene {self.pto} puntos"   
class peliculas:
    def __init__(self, pelicula, titulo, sala, hora):
        self.peli=pelicula
        self.title=titulo
        self.sala=sala
        self.hr=hora
    def ver_peli(self):
        return f"Prepárate para ver la pelicula de {self.title} en la sala {self.sala} a las {self.hr}"
    

class Sala:
    def __init__(self, numero, tipo):
        self.num = numero
        self.tipo= tipo
        
        self.asientos =["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5"]
        self.ocupado =[]

    def verificar_asiento(self, asiento):
        if asiento in self.ocupado:
            return False
        else:
            return True
    def negar_asiento(self, asiento):
        if asiento not in self.ocupado:
            self.ocupado.append(asiento)
            return True
        else:
            return False


class Reserva:
    def __init__(self, id_reserva, asientos, usuario, película):
        self.id_reserva=id_reserva
        self.asientos=asientos
        self.usuario=usuario
        self.peli=película
       
        self.final =0

    def calcular_total(self, precio_del_ugar):
        self.final=precio_del_ugar* len(self.asientos)

    def descuento_aplicado(self, porcentaje):
        descuento= self.final *porcentaje/100
        self.total=self.final-descuento

    def ticket_generado(self):
        return f"""
    Compra aplicada
Nombre :{self.usuario.nom}
Película: {self.peli.title}
Asientos: {self.asientos}
Total a pagar: {self.final} pesos
Estado: Pagado
"""