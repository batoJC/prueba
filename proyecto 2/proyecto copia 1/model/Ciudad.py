import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from model.Tanque import Tanque
from model.Barrio import Barrio
from model.Tubo import Tubo
from model.Gota import Gota
import time

class Ciudad:

    def __init__(self,canvas):
        print('iniciar ciudad')
        self.obstruccion = False
        self.nAristas = 1
        self.nVertices = 1
        self.gotas = []
        self.vertices = {} #se guardan los vertices clave : valor
        self.aristas = {} #se guarda las aristas con el (origen,destino) como clave
        self.canvas = canvas
        self.espacios = []
        self.barrio = ImageTk.PhotoImage(Image.open(os.getcwd() + '\images\edificio.png').resize((60, 60)))
        self.barriod = ImageTk.PhotoImage(Image.open(os.getcwd() + '\images\edificio.png').resize((60, 60)))
        self.pintar()

    def eliminar(self):
        self.aristas = {}
        self.vertices = {}
        self.nAristas = 1
        self.nVertices = 1
        self.gotas = []
        self.espacios = []
        self.vertices = {}  # se guardan los vertices clave : valor
        self.aristas = {}  # se guarda las aristas con el (origen,destino) como clave
        self.pintar()

    def pintar(self):
        self.obstruccion = True
        time.sleep(1)
        self.gotas = []
        self.canvas.delete('all')
        self.crearCuadricula()
        self.pintarTubos()
        self.pintarVertices()
        self.obstruccion = False

    def crearCuadricula(self):
        aux = []
        for v in range(1,20):
            aux.append(0)
            self.canvas.create_line(v*60,0,v*60,670,fill='#30af27')
        for h in range(1,12):
            self.espacios.append(aux.copy())
            self.canvas.create_line(0,h*60,1160,h*60,fill='#30af27')

    def pintarVertices(self):
        for n,v in self.vertices.items():
            print(v)
            if n[0] == 'T':
                print('pintar tanque')
                v.pintar(self.canvas,True)
                v.x = None
            if n[0] == 'B':
                self.canvas.create_image(60 * v.columna, 60 * v.fila, image=self.barrio, anchor=NW)
                v.x = None
                v.pintarX(self.canvas)
            self.canvas.create_text( 60 * v.columna +7, 60 * v.fila+7, text=n, fill="white",
                                    font="Times 7 italic bold")

    def pintarTubos(self):
        aux = {}

        for n,v in self.aristas.items():
            origen = self.vertices[n[0]]
            destino = self.vertices[n[1]]

            texto = "(" + n[0] + "," + n[1] + ")"
            aux1 = aux.get((n[0],n[1]))
            aux2 = self.aristas.get((n[1],n[0]))
            if aux1 == None and aux2 != None:
                texto += ",(" + n[1] + "," + n[0] + ")"
                aux[n[1],n[0]] = 'S'

            if aux1 == None:
                self.canvas.create_line(origen.columna*60+30,origen.fila*60+60,destino.columna*60+30,destino.fila*60+60,fill='#403c3c',width=5)
                origen = (origen.columna*60+30,origen.fila*60+60)
                destino = (destino.columna*60+30,destino.fila*60+60)

                enX = (origen[0] - destino[0])/2
                enY = (origen[1] - destino[1])/2
                self.canvas.create_text(destino[0]+enX, destino[1]+enY, text=texto, fill="white",
                                        font="Times 11 italic bold")

    def agregarTanque(self, capacidad, cantidad, fila, columna):
        print('agregar tanque')
        if self.espacios[fila - 1][columna - 1] == 0:
            self.espacios[fila - 1][columna - 1] = 1
            self.vertices['T'+str(self.nVertices)] = Tanque(capacidad, cantidad, fila-1,columna-1)
            self.nVertices += 1
        else:
            messagebox.showerror(message='Ya existe un elemento en esa posición',
                                 title="Error")

    def agregarBarrio(self, consumo, fila, columna):
        print('agregar barrio')
        if self.espacios[fila-1][columna-1] == 0:
            self.espacios[fila-1][columna-1] = 1
            self.vertices['B'+str(self.nVertices)] = Barrio(self.canvas, consumo, fila-1, columna-1,'B'+str(self.nVertices))
            self.nVertices += 1
        else:
            messagebox.showerror(message='Ya existe un elemento en esa posición',title="Error")

    def agregarTubo(self, capacidad, origen, destino):
        print('agregar tubo')
        if len(self.aristas) > 0:
            o = self.vertices.get(origen)
            d = self.vertices.get(destino)
            if o is None or d is None:
                messagebox.showerror(message='Uno de los vertices no existe',title="Error")
                return
            aux = self.aristas.get((origen, destino))
            if aux is None:
                self.aristas[(origen,destino)] = Tubo(capacidad,self.vertices[origen],self.vertices[destino])
                self.vertices[origen].adyacentes.append(destino)
            else:
                if aux.estado:
                    messagebox.showerror(message='Ya existe un tubo en esta dirección y esta en correcto funcionamiento',title="Error")
                else:
                    self.aristas[(origen, destino)] = Tubo(capacidad, self.vertices[origen],self.vertices[destino])
        else:
            self.aristas[(origen, destino)] = Tubo(capacidad, self.vertices[origen], self.vertices[destino])
            self.vertices[origen].adyacentes.append(destino)

    def moverGotas(self):
        for gota in self.gotas:
            gota.mover(self.canvas)
            # c.coords(x)
            aux = self.canvas.coords(gota.id)
            if aux[2] == gota.destino.columna*60+30 and aux[3] == gota.destino.fila*60+60:
                print(type(gota.destino))
                print('tipo')
                if isinstance(gota.destino, Tanque):
                    print('tanque')
                    gota.destino.cantidad += gota.cantidad
                    gota.destino.pintar(self.canvas,False)
                    if gota.destino.cantidad > gota.destino.capacidad:
                        gota.destino.cantidad = gota.destino.capacidad
                        gota.destino.pintarGota(self.canvas)
                    else:
                        gota.destino.quitarGota(self.canvas)
                if isinstance(gota.destino, Barrio):
                    print('barrio')
                    cantidad = gota.cantidad
                    gota.destino.quitarX(self.canvas)
                    gota.destino.estado = True
                    cantidad -= gota.destino.consumo
                    if cantidad >= 0:
                        for d in gota.destino.adyacentes:
                            auxCantidad = self.aristas.get((gota.destino.nombre,d)).capacidad
                            if cantidad < auxCantidad:
                                self.gotas.append(Gota(self.canvas, cantidad, gota.destino, self.vertices.get(d)))
                                cantidad = 0
                                break
                            else:
                                cantidad -= auxCantidad
                                self.gotas.append(Gota(self.canvas, auxCantidad, gota.destino, self.vertices.get(d)))
                    if cantidad > 0:
                        gota.destino.pintarGota(self.canvas)
                self.canvas.delete(gota.id)
                self.gotas.remove(gota)

    def enviarGotas(self):
        for n,v in self.vertices.items():
            if n[0] == 'T':
                tanque = self.vertices.get(n)
                for destino in v.adyacentes:
                    cantidad = self.aristas.get((n,destino)).capacidad
                    print(cantidad)
                    if tanque.cantidad == 0:
                        tanque.pintarX(self.canvas)
                    else:
                        if v.capacidad > v.cantidad:
                            v.quitarGota(self.canvas)
                        tanque.quitarX(self.canvas)
                        if cantidad <= tanque.cantidad:
                            tanque.cantidad -= cantidad
                            tanque.pintar(self.canvas,False)
                            self.gotas.append(Gota(self.canvas, cantidad,self.vertices.get(n),self.vertices.get(destino)))
                        else :
                            self.gotas.append(Gota(self.canvas, tanque.cantidad,self.vertices.get(n),self.vertices.get(destino)))
                            tanque.cantidad = 0
                            tanque.pintar(self.canvas,False)

    def revisarBarrios(self):
        for n,v in self.vertices.items():
            if n[0] == 'B':
                if v.estado == False:
                    v.pintarX(self.canvas)
                else:
                    v.estado = False



    def run(self):
        cont = 0
        while not self.obstruccion:
            if cont == 0:
                self.enviarGotas()
                self.revisarBarrios()
                cont = 10
            self.moverGotas()
            cont -= 2
            time.sleep(0.1)


