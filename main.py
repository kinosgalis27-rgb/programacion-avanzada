from models import *

print("usuarios")
u1=usuario(1,"Carlos",150)
u2=usuario(2,"Ana",120)
u3=usuario(3,"Kino",90)
u4=usuario(4,"Chokis",80)
u5=usuario(5,"Miguel",70)
u6=usuario(6,"jaime Alejandro",60)
u7=usuario(7,"Pedro Parker",50)
u8 =usuario(8,"Maria",40)
u9=usuario(9,"Diego",30)
u10=usuario(10,"Elena",20)

print(u1.ver_informacion())
print(u2.ver_informacion())
print(u3.ver_informacion())
print(u4.ver_informacion())
print(u5.ver_informacion())
print(u6.ver_informacion())
print(u7.ver_informacion())
print(u8.ver_informacion())
print(u9.ver_informacion())
print(u10.ver_informacion())


print("Peliculas")

p1=peliculas(1,"Dune",1,"18:00")
p2=peliculas(2,"Avatar",2,"19:00")
p3=peliculas(3,"Batman",3,"20:00")
p4=peliculas(4,"Spiderman",4,"21:00")
p5=peliculas(5,"Oppenheimer",5,"17:00")
p6=peliculas(6,"Matrix",1,"16:00")
p7=peliculas(7,"Interstellar",2,"22:00")
p8 =peliculas(8,"Joker",3,"18:30")
p9 =peliculas(9,"Titanic",4,"19:30")
p10 =peliculas(10,"Frozen",5,"15:00")

print(p1.ver_peli())
print(p2.ver_peli())
print(p3.ver_peli())
print(p4.ver_peli())
print(p5.ver_peli())
print(p6.ver_peli())
print(p7.ver_peli())
print(p8.ver_peli())
print(p9.ver_peli())
print(p10.ver_peli())


print("Salas")

s1 = Sala(1,"Normal")
s2 = Sala(2,"Normal")
s3 = Sala(3,"3D")
s4 = Sala(4,"IMAX")
s5 = Sala(5,"VIP")
s6 = Sala(6,"Normal")
s7 = Sala(7,"Normal")
s8 = Sala(8,"3D")
s9 = Sala(9,"IMAX")
s10 = Sala(10,"VIP")



print("Disponibilidad de lugares")
if s1.verificar_asiento("a1"):
    s1.negar_asiento("a1")
    print("Asiento a1 reservado")
else:
    print("Asiento a1 ocupado")

if s1.verificar_asiento("a2"):
    s1.negar_asiento("a2")
    print("Asiento a2 reservado")
else:
    print("Asiento a2 ocupado")


print("reservaciones")

r1 = Reserva(1,["a1","a2"],u1,p1)
r2 = Reserva(2,["a3"],u2,p2)
r3 = Reserva(3,["b1"],u3,p3)
r4 = Reserva(4,["b2"],u4,p4)
r5 = Reserva(5,["a4"],u5,p5)
r6 = Reserva(6,["b3"],u6,p6)
r7 = Reserva(7,["a5"],u7,p7)
r8 = Reserva(8,["b4"],u8,p8)
r9 = Reserva(9,["b5"],u9,p9)
r10 = Reserva(10,["a3"],u10,p10)


print("precio")

r1.calcular_total(80)
r2.calcular_total(80)
r3.calcular_total(80)
r4.calcular_total(80)
r5.calcular_total(80)
r6.calcular_total(80)
r7.calcular_total(80)
r8.calcular_total(80)
r9.calcular_total(80)
r10.calcular_total(80)


print("Descuento aplicado")

r1.descuento_aplicado(20)
print("Descuento aplicado a la reserva 1")


print("ticket generado")

print(r1.ticket_generado())
print(r2.ticket_generado())
print(r3.ticket_generado())
print(r4.ticket_generado())
print(r5.ticket_generado())
print(r6.ticket_generado())
print(r7.ticket_generado())
print(r8.ticket_generado())
print(r9.ticket_generado())
print(r10.ticket_generado())

print("aña")