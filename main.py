import random


class Cartas:
    def __init__ (self,tipo,cont,extra):
        self.t = tipo  #para filtrar por tipo
        self.c = cont  #
        self.u = 1     #si está usada o no
        self.extra = extra #multiplicador/comodín(asociado a jugador)/ cambio de modo
    def usar (self):
        self.u = self.u * (-1)
        print(self.c)
    def re ():
        self.u = 1


class Jugadores:
    def __init__ (self, nombre):
        self.n = nombre
        self.ext = []
        self.c = 0
    def ex (self,com,type):
        if type == 1:
            self.extr.append(com)
        else:
            self.extr.remove(com)
    def tr():
        self.c += 1



i = 0
j = 0
modo = 0
c, cs, cp, cy, cc = [], [], [], [], []
kst = []
def load (modo):   
    with open("./reto.txt") as f:
        data = f.read()
        print(data)
    if modo == 1:
        c = c + cs
    random.shuffle(c)
    random.shuffle(cp)
    random.shuffle(cy)
    random.shuffle(cc)
    nombre = input()
    kst.append(Jugadores(nombre))


reshuffle = len(c)

def main():
    print(2)
        

def juego():
    j = (j+1) % len(kst)
    i += 1
    if i == reshuffle:
        i = 0
        for ca in c:
            ca.re()
        c.shuffle()
    c[i].usar()
    pro =c[i].extra
    opt =  c[i].t
    if opt == "d":
        2+1
    elif opt == "p":
        cp[i%len(cp)].usar()
    elif opt == "y":
        cy[i%len(cy)].usar()
    elif opt == "c":
        kst[j].ex(1,pro)
            

                
