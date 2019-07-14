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

    def __init__(self,canvas, info):
        self.info = info
        self.listaIdVertices = []
        self.obstruccion = False
        self.nAristas = 1
        self.nVertices = 1
        self.gotas = []
        self.rutas = []
        self.afectados = []
        self.vertices = {} #se guardan los vertices clave : valor
        self.aristas = {} #se guarda las aristas con el (origen,destino) como clave
        self.canvas = canvas
        self.espacios = []
        self.crearCuadricula()

    def eliminar(self):
        self.canvas.delete('all')
        self.espacios = []
        self.crearCuadricula()
        self.aristas = {}
        self.vertices = {}
        self.nAristas = 1
        self.nVertices = 1
        self.gotas = []
        self.vertices = {}  # se guardan los vertices clave : valor
        self.aristas = {}  # se guarda las aristas con el (origen,destino) como clave
        self.pintar()

    def pintar(self):
        self.obstruccion = True
        time.sleep(1)
        self.pintarTubos()
        self.pintarVertices()
        self.pintarGotas()
        self.obstruccion = False

    def pintarGotas(self):
        aux = []
        for gota in self.gotas:
            coord = self.canvas.coords(gota.id)
            self.canvas.delete(gota.id)
            aux1 = Gota(self.canvas,gota.cantidad,gota.origen,gota.destino)
            aux1.setPosition(coord[0],coord[1],coord[2],coord[3],self.canvas)
            aux.append(aux1)
            # print(coord)
            # gota.setPosition(coord[0],coord[1],coord[2],coord[3],self.canvas)
        self.gotas = aux

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
            if n[0] == 'T':
                v.pintar(self.canvas,True)
            if n[0] == 'B':
                v.pintar(self.canvas)
                v.pintarX(self.canvas)
            self.canvas.create_text( 60 * v.columna +7, 60 * v.fila+7, text=n, fill="white",
                                     font="Times 7 italic bold")

    def pintarTubos(self):
        # limpiar las aristas
        for id in self.listaIdVertices:
            self.canvas.delete(id)

        aux = {}

        for n,v in self.aristas.items():
            origen = self.vertices[n[0]]
            destino = self.vertices[n[1]]

            texto = "(" + n[0] + "-" + n[1] + ","+str(v.capacidad)+")"
            aux1 = aux.get((n[0],n[1]))
            aux2 = self.aristas.get((n[1],n[0]))
            if aux1 == None and aux2 != None:
                texto += ",(" + n[1] + "-" + n[0] + ","+str(v.capacidad)+")"
                aux[n[1],n[0]] = 'S'

            if aux1 == None:
                id = self.canvas.create_line(origen.columna*60+30,origen.fila*60+60,destino.columna*60+30,destino.fila*60+60,fill='#403c3c',width=5)
                self.listaIdVertices.append(id)
                origen = (origen.columna*60+30,origen.fila*60+60)
                destino = (destino.columna*60+30,destino.fila*60+60)

                enX = (origen[0] - destino[0])/2
                enY = (origen[1] - destino[1])/2
                # self.canvas.create_text(destino[0]+enX, destino[1]+enY, text=texto, fill="white",
                #                         font="Times 11 italic bold")
                id = self.canvas.create_text(destino[0] + enX, destino[1] + enY, text=texto, fill="white",
                                             font="Times 11 italic bold")
                self.listaIdVertices.append(id)

    def agregarTanque(self, capacidad, cantidad, fila, columna):
        if self.espacios[fila - 1][columna - 1] == 0:
            self.espacios[fila - 1][columna - 1] = 1
            self.vertices['T'+str(self.nVertices)] = Tanque('T'+str(self.nVertices),self.canvas,capacidad, cantidad, fila-1,columna-1)
            self.nVertices += 1
        else:
            messagebox.showerror(message='Ya existe un elemento en esa posición',
                                 title="Error")

    def agregarBarrio(self, consumo, fila, columna):
        if self.espacios[fila-1][columna-1] == 0:
            self.espacios[fila-1][columna-1] = 1
            self.vertices['B'+str(self.nVertices)] = Barrio(self.canvas, consumo, fila-1, columna-1,'B'+str(self.nVertices))
            self.nVertices += 1
        else:
            messagebox.showerror(message='Ya existe un elemento en esa posición',title="Error")

    def agregarTubo(self, capacidad, origen, destino):
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
                if isinstance(gota.destino, Tanque):
                    gota.destino.cantidad += gota.cantidad
                    gota.destino.pintar(self.canvas,False)
                    if gota.destino.cantidad > gota.destino.capacidad:
                        gota.destino.cantidad = gota.destino.capacidad
                        gota.destino.pintarGota(self.canvas)
                    else:
                        gota.destino.quitarGota(self.canvas)
                if isinstance(gota.destino, Barrio):
                    cantidad = gota.cantidad
                    gota.destino.quitarX(self.canvas)
                    gota.destino.estado = True
                    cantidad -= gota.destino.consumo
                    if cantidad >= 0:
                        for d in gota.destino.adyacentes:
                            if self.aristas[(gota.destino.nombre,self.vertices.get(d).nombre)].estado:
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
                    if self.aristas[(tanque.nombre,self.vertices.get(destino).nombre)].estado:
                        cantidad = self.aristas.get((n,destino)).capacidad
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

    def cambiarSentido(self,clave):
        self.obstruccion = True
        time.sleep(1)
        tubo = self.aristas[clave]
        aux = tubo.destino
        i = 0
        for gota in self.gotas:
            if gota.origen.nombre == tubo.origen.nombre and gota.destino.nombre == tubo.destino.nombre:
                gota.origen = tubo.destino
                gota.destino = tubo.origen

        for vertice in tubo.origen.adyacentes:
            if vertice == aux.nombre:
                break
            i += 1
        tubo.origen.adyacentes.pop(i)
        del self.aristas[clave]
        self.agregarTubo(tubo.capacidad,tubo.destino.nombre,tubo.origen.nombre)
        self.pintar()


    def run(self):
        cont = 0
        while True:
            if not self.obstruccion:
                if cont == 0:
                    self.enviarGotas()
                    self.revisarBarrios()
                    cont = 10
                self.moverGotas()
                cont -= 2
                time.sleep(0.1)


    # GENERAR OBSTRUCCIONES
    def generarObstrucciones(self,clave):
        self.obstruccion = True
        aux = self.aristas[clave]
        aux.pintarX(self.canvas)
        aux.estado = False
        time.sleep(2)
        # quitar de la lista de adyacencias del origen
        origen = self.vertices.get(clave[0])
        destino = self.vertices.get(clave[1])
        i = 0
        for ad in origen.adyacentes:
            if ad == destino.nombre:
                break
            i += 1
        origen.adyacentes.pop(i)

        # quitar las gotas del tubo
        eliminar = []
        for j in range(0,self.gotas.__len__()):
            if self.gotas[j].origen.nombre == origen.nombre and self.gotas[j].destino.nombre == destino.nombre:
                self.canvas.delete(self.gotas[j].id)
                eliminar.append(j)
        restar = 0
        for indice in eliminar:
            self.gotas.pop(indice-restar)
            restar += 1
        #resaltar las rutas por las que deberia llegar agua a los barrios afectados

        #buscar barrios afectados
        self.recorrido = []
        self.visitados = []
        self.profundidad(destino)
        afectados = self.visitados.copy()
        self.afectados.extend(afectados)
        pesos , adyacencias = self.generarMatrices()
        adyacencias = self.getAdyacencias(pesos.copy(),adyacencias.copy())
        for id in self.rutas:
            self.canvas.delete(id)
        for vertice in self.afectados:
            if vertice[0] == 'B':
                print('Barrio')
                for r in self.getRutas(adyacencias,vertice):
                    self.pintarRecorrido(r)

        texto = 'propuestas de tubos\r\n entre tanques\r\n'
        # proponer conexiones entre tanques para repartir el agua acumulada
        for v in self.vertices.values():
            if isinstance(v,Tanque) and v.adyacentes.__len__()==0:
                for v2 in self.vertices.values():
                    if isinstance(v2, Tanque):
                        if v.nombre != v2.nombre and v2.adyacentes.__len__() > 0:
                            cantidad = 0
                            for ad in v2.adyacentes:
                                aux = self.aristas[(v2.nombre,ad)]
                                if aux.estado:
                                    cantidad += aux.capacidad
                            texto += "("+v.nombre+","+v2.nombre+","+str(cantidad)+")\r\r"

        texto += "Propuestas para nuevas \r\nubicaciones para los tanques \r\n"

        valores = []
        #primer cuadrante
        valores.append(self.calcularNecesidad(1,1,10,6))

        #segundo cuadrante
        valores.append(self.calcularNecesidad(11,1,19,6))

        #tercero cuadrante
        valores.append(self.calcularNecesidad(1,7,10,11))

        #cuarto cuadrante
        valores.append(self.calcularNecesidad(11,7,19,11))

        for valor in valores:
            texto = self.evaluar(texto,valor)

        self.info.config(text=texto)
        time.sleep(0.1)
        self.obstruccion = False

    def evaluar(self,texto,valores):
        if valores[0] > 0:
            if not valores[1] is None:
                texto += "Columna: "+str(valores[1][0])+" \r\n"
                texto += "Fila: "+str(valores[1][1])+" \r\n"
                texto += "Capacidad: "+str(valores[0])+" \r\n"
        return texto

    def profundidad(self, nodo):
        self.visitados = []
        recorrer = []
        self.visitados.append(nodo.nombre)
        recorrer.extend(nodo.adyacentes)
        for aux in recorrer:
            if not self.visitado(aux):
                aux = self.vertices[aux]
                self.visitados.append(aux.nombre)
                recorrer.extend(aux.adyacentes)

    def visitado(self, string):
        for nodo in self.visitados:
            if nodo == string:
                return True
        return False

    def pintarRecorrido(self, lista):
        print(lista)
        ant = None
        for v in lista:
            if ant is None:
                ant = self.vertices[v]
            else:
                aux = self.vertices[v]
                COSA = self.aristas.get((ant.nombre,aux.nombre))
                if not COSA is None:
                    if COSA.estado:
                        self.rutas.append(self.canvas.create_line(ant.columna*60+30, ant.fila*60+60, aux.columna*60+30, aux.fila*60+60, fill='yellow', width=1))
                        ant = aux


    # floyd warshall
    def generarMatrices(self):
        pesos = []
        auxNodos = []
        adyacencias = []
        for n in self.vertices:
            auxNodos.append(n)
        for no in self.vertices:
            adyacencias.append(auxNodos.copy())

        auxLista = []
        for tubo in self.aristas.values():
                auxLista.append(tubo.capacidad)


        for i in range(0,auxLista.__len__()):
            for j in range(0, auxLista.__len__()):
                if i != j and auxLista[i] < auxLista[j]:
                    aux = auxLista[i]
                    auxLista[i] = auxLista[j]
                    auxLista[j] = aux
        auxCambioPesos = {}
        for m in range(0,auxLista.__len__()):
            auxCambioPesos[auxLista[m]] = auxLista[auxLista.__len__()-1-m]

        i = 0
        for nodo in self.vertices.values():
            auxPesos = []
            adyacencias[i][i] = ''
            for nodo1 in self.vertices.values():
                if nodo.nombre == nodo1.nombre:
                    auxPesos.append(0)
                else:
                    arista = self.aristas.get((nodo.nombre, nodo1.nombre))
                    if arista is None:
                        auxPesos.append(float('inf'))
                    elif arista.estado:
                        auxPesos.append(auxCambioPesos[arista.capacidad])
                    else:
                        auxPesos.append(float('inf'))
            pesos.append(auxPesos.copy())
            i += 1
        print(pesos)
        return pesos,adyacencias

    def getAdyacencias(self, pesos, adyacencias):
        fin = self.vertices.__len__()
        for i in range(0,fin):# para el nodo fila y columna
            for j in range(0, fin):
                for k in range(0, fin):
                    if j != i and k != i:
                        if pesos[j][k] > (pesos[j][i]+pesos[i][k]):
                            pesos[j][k] = pesos[j][i] + pesos[i][k]
                            adyacencias[j][k] = self.getNombre(i)
        return adyacencias

    def getRutas(self,adyacencias, destino):
        indice = self.getIndice(destino)
        salida = []
        for n in self.vertices:
            if n[0] == 'T':
                aux = []
                origen = n
                aux.append(origen)
                tubo = self.aristas.get((origen, adyacencias[self.getIndice(origen)][indice]))
                while not tubo is None:
                    origen = adyacencias[self.getIndice(origen)][indice]
                    aux.append(origen)
                    if origen == destino:
                       salida.append(aux)
                       break
        return salida

    def getIndice(self, nombre):
        indice = 0
        for n in self.vertices:
            if n == nombre:
                break
            indice += 1
        return indice

    def getNombre(self, indice):
        for n in self.vertices:
            if indice == 0:
                return n
            indice -= 1

    def calcularNecesidad(self, x1,y1,x2,y2):
        consumo = 0
        disponible = 0
        ubicacion = None
        for i in range(x1,x2+1):
            for j in range(y1, y2+1):
                for vertice in self.vertices.values():
                    if vertice.columna == i and vertice.fila == j:
                        if isinstance(vertice, Barrio):
                            consumo += vertice.consumo
                        if isinstance(vertice, Tanque):
                            disponible += vertice.cantidad
                    else:
                        ubicacion = (i,j)

        consumo *= 15
        if consumo > disponible:
            return consumo - disponible,ubicacion
        else:
            return 0,ubicacion
