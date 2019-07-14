from tkinter import *
from PIL import Image, ImageTk
import os


class Tanque:

    def __init__(self, nombre, canvas, capacidad, cantidad, fila, columna):
        self.id = None
        self.nombre = nombre
        self.grafico={}
        self.fila = fila
        self.columna = columna
        self.capacidad = capacidad
        self.cantidad = cantidad
        self.pintar(canvas,True)
        self.adyacentes = []
        self.x = None
        self.gota = None
        self.gotaImagen = ImageTk.PhotoImage(Image.open(os.getcwd() + '\images\water.png').resize((15, 20)))

    def pintar(self,canvas,op):
        if op:
            for id in self.grafico:
                canvas.delete(id)

            self.grafico['tanque'] = canvas.create_rectangle(self.columna * 60 + 10, self.fila * 60 + 10,
                                                             self.columna * 60 + 50, self.fila * 60 + 60, fill='grey')
            valor = (self.cantidad * 50) / self.capacidad
            if valor > 50:
                self.pintarGota(canvas)
                valor = 50
            self.grafico['agua'] = canvas.create_rectangle(self.columna * 60 + 12, self.fila * 60 + 10 + (50 - valor),
                                                           self.columna * 60 + 48, self.fila * 60 + 58, fill="blue")
            self.grafico['vacio'] = canvas.create_rectangle(self.columna * 60 + 12, self.fila * 60 + 10,
                                                            self.columna * 60 + 48,
                                                            self.fila * 60 + 59 - valor, fill="black")
        else:
            valor = (self.cantidad * 50) / self.capacidad
            if valor > 50:
                self.pintarGota(canvas)
                valor = 50
            canvas.coords(self.grafico['agua'],self.columna * 60 + 12, self.fila * 60 + 10 + (50 - valor),
                                                           self.columna * 60 + 48, self.fila * 60 + 58)
            canvas.coords(self.grafico['vacio'],self.columna * 60 + 12, self.fila * 60 + 10,
                                                            self.columna * 60 + 48,
                                                            self.fila * 60 + 59 - valor)

    def pintarX(self,canvas):
        if self.x is None:
            self.x = canvas.create_line(self.columna*60+15,self.fila*60+15,self.columna*60+45,self.fila*60+45,fill="red",width=2),canvas.create_line(self.columna*60+45,self.fila*60+15,self.columna*60+15,self.fila*60+45,fill="red",width=2)
            self.quitarGota(canvas)

    def quitarX(self,canvas):
        if not self.x is None:
            canvas.delete(self.x[0])
            canvas.delete(self.x[1])
            self.x = None

    def pintarGota(self, canvas):
        if self.gota is None:
            self.gota = canvas.create_image(60 * self.columna+50, 60 * self.fila, image=self.gotaImagen, anchor=NW)

    def quitarGota(self, canvas):
        if not self.gota is None:
            canvas.delete(self.gota)
            self.gota = None
