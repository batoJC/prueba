class Tubo:

    def __init__(self, capacidad, origen, destino):
        self.id = 0
        self.capacidad = capacidad
        self.origen = origen
        self.destino = destino
        self.estado = True


    def pintarX(self, canvas):
        origen = (self.origen.columna*60+30,self.origen.fila*60+60)
        destino = (self.destino.columna*60+30,self.destino.fila*60+60)
        enX = (origen[0] - destino[0])/2
        enY = (origen[1] - destino[1])/2
        canvas.create_line(destino[0] + enX-8, destino[1] + enY-8, destino[0] + enX+8, destino[1] + enY+8, fill="red", width=2)
        canvas.create_line(destino[0] + enX+8, destino[1] + enY-8, destino[0] + enX-8, destino[1] + enY+8, fill="red",width=2)




