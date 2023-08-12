import random


class Cartas ():
    def __init__ (self,tipo,cont,uso,extra):
        self.tipo = tipo
        self.cont = cont
        self.uso = uso 
        self.extra = extra #multiplicador/comodín(asociado a jugador)
    def uso(nombre):
        nombre.update()
        self.uso = 0
        

class Jugadores ():
    def __init__ (self, nombre,extra,contar):
        self.nombre = nombre
        self.extra = extra
        self.contar = contar
    def update (tragos,):
        self.contar += tragos


def load ():
    with open("./reto.txt") as f:
        data = f.read()
        print(data)
    cat1,cat2,cat3,cat4,cat5 = []
