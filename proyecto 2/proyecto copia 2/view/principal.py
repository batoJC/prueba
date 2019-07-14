# inicia el proyecto
from tkinter import *
from view.modalAgregarTubo import modalAgregarTubo
from view.modalAgregarBarrio import modalAgregarBarrio
from view.modalAgregarTanque import modalAgregarTanque
from view.modalCambiarSentido import modalCambiarSentido
from view.modalGenerarObstruccion import modalGenerarObstruccion
from model.Ciudad import Ciudad
import json
import os
import threading

class principal:

    def __init__(self):
        #iniciar la ventana maximizada
        self.app = Tk()
        self.app.title('Ciudad')
        self.app.state('zoomed')
        # aquí se agrega el menu
        menu = Frame(bg='red', width=1366)
        menu.grid(column=6, row=1, padx=(50, 50), pady=(10, 10))
        menu.pack()

        # boton 1 cargar datos por json
        btn_click1 = Button(menu, text='Cargar Datos por json', command=self.cargarJson)
        btn_click1.grid(column=1, row=1)

        # boton 2 agregar tubo
        btn_click2 = Button(menu, text='Agregar Tubo', command=self.agregarTubo)
        btn_click2.grid(column=2, row=1)

        # boton 3 agregar barrio
        btn_click3 = Button(menu, text='Agregar Barrio', command=self.agregarBarrio)
        btn_click3.grid(column=3, row=1)

        # boton 4 agregar tanque
        btn_click4 = Button(menu, text='Agregar Tanque', command=self.agregarTanque)
        btn_click4.grid(column=4, row=1)

        # boton 5 cambiar de sentido a un tubo
        btn_click5 = Button(menu, text='Cambiar de sentido', command=self.cambiarSentido)
        btn_click5.grid(column=5, row=1)

        # boton 6 simular obstrucción
        btn_click = Button(menu, text='Simular Obstrucción', command=self.generarObstruccion)
        btn_click.grid(column=6, row=1)

        # boton 6 simular obstrucción
        btn_click = Button(menu, text='INICIAR', command=self.iniciar)
        btn_click.grid(column=7, row=1)

        contenido = Frame(width=1366, height=670)
        contenido.pack()

        # todoo aquí se muestra información sobre el grafo
        info = Frame(contenido, bg='blue', width=220, height=665)
        info.place(x=0, y=0)
        self.photo = PhotoImage("edificio.png")
        labelinfo = Label(info)
        labelinfo.pack()
        labelinfo.config(text="")

        # aquí se dibuja todoo lo relacionado con el grafo 1160,670
        self.canvas = Canvas(contenido, width=1139, height=659, bg='#000000')
        self.ciudad = Ciudad(self.canvas,labelinfo)
        # self.ciudad.pintar()
        self.canvas.place(x=222, y=0)

        self.app.mainloop()

    def cargarJson(self):
        print('cargar JSON')
        # self.ciudad.pintar()
        # self.app.update()
        self.ciudad.eliminar()
        with open(os.getcwd()+'\data\data.json') as contenido:
            datos = json.load(contenido)
            datos = datos[0]
            for barrio in datos.get('barrios'):
                self.ciudad.agregarBarrio(barrio['consumo'],barrio['fila'],barrio['columna'])
            for tanque in datos.get('tanques'):
                self.ciudad.agregarTanque(tanque['capacidad'], tanque['cantidad'], tanque['fila'], tanque['columna'])
            for tubo in datos.get('tubos'):
                self.ciudad.agregarTubo(tubo['capacidad'], tubo['origen'], tubo['destino'])
            self.ciudad.pintar()
            return

    def agregarTubo(self):
        print('agregar Tubo')
        ventana = modalAgregarTubo(self.app)
        if ventana.res:
            self.ciudad.agregarTubo(ventana.capacidad,ventana.origen,ventana.destino)
            self.ciudad.pintar()

    def agregarBarrio(self):
        print('agregar Barrio')
        ventana = modalAgregarBarrio(self.app)
        if ventana.res:
            self.ciudad.agregarBarrio(ventana.consumo, ventana.fila, ventana.columna)
            self.ciudad.pintar()

    def agregarTanque(self):
        print('agregar Tanque')
        ventana = modalAgregarTanque(self.app)
        if ventana.res:
            self.ciudad.agregarTanque(ventana.capacidad, ventana.cantidad, ventana.fila, ventana.columna)
            self.ciudad.pintar()

    def generarObstruccion(self):
        print('Generar obstrucción')
        ventana = modalGenerarObstruccion(self.app, self.ciudad.aristas.keys())
        if ventana.res:
            print(ventana.tubo)
            self.ciudad.generarObstrucciones(ventana.tubo)


    def cambiarSentido(self):
        print('cambiar Sentido')
        ventana = modalCambiarSentido(self.app, self.ciudad.aristas.keys())
        if ventana.res:
            # self.ciudad.obstruccion = True
            # print(ventana.tubo)
            self.ciudad.cambiarSentido(ventana.tubo)


    def iniciar(self):
        self.ciudad.obstruccion = False
        self.t = threading.Thread(target=self.ciudad.run, name='Servicio')
        self.t.start()



