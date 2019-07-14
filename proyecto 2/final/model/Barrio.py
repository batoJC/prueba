import os
from tkinter import *
from tkinter import messagebox
    from PIL import Image, ImageTk


class Barrio:

    def __init__(self, canvas, consumo,fila,columna, nombre):
        self.id = None
        self.nombre = nombre
        self.barrio = ImageTk.PhotoImage(Image.open(os.getcwd() + '\images\edificio.png').resize((60, 60)))
        self.fila = fila
        self.columna = columna
        self.consumo = consumo
        self.adyacentes = []
        self.x = None
        self.estado = False
        # print(os.getcwd()+ '\images\agua.png')
        self.gota = None
        self.gotaImagen = ImageTk.PhotoImage(Image.open(os.getcwd() + '\images\edificiod.png').resize((60, 60)))
        self.pintar(canvas)

    def pintar(self, canvas):
        if not self.id is None:
            canvas.delete(self.id)
        self.id = canvas.create_image(60 * self.columna, 60 * self.fila, image=self.barrio, anchor=NW)
        self.quitarX(canvas)

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
            self.gota = canvas.create_image(60 * self.columna, 60 * self.fila, image=self.gotaImagen, anchor=NW)
            self.quitarX(canvas)

    def quitarGota(self, canvas):
        if not self.gota is None:
            canvas.delete(self.gota)

