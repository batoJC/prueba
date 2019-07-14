import math

class Gota:

    def __init__(self, canvas, cantidad, origen, destino):
        f1 = (origen.columna * 60 + 30, origen.fila * 60 + 60)
        f2 = (destino.columna * 60 + 30, destino.fila * 60 + 60)
        pendiente = self.pendiente(f1,f2,False)
        self.id = canvas.create_line(origen.columna*60+30,origen.fila*60+60,origen.columna*60+30+pendiente[0],origen.fila*60+60+pendiente[1],fill='blue',width=5)
        self.cantidad = cantidad
        self.origen = origen
        self.destino = destino

    def setPosition(self, x1, y1, x2, y2, canvas):
        print('cambiar la posicion')
        canvas.coords(self.id,x1,y1,x2,y2)

    def mover(self,canvas):
        origen = (self.origen.columna * 60 + 30, self.origen.fila * 60 + 60)
        destino = (self.destino.columna * 60 + 30, self.destino.fila * 60 + 60)
        pendiente = self.pendiente(origen,destino,True)
        canvas.move(self.id,-pendiente[0] ,-pendiente[1] )

    def pendiente(self, origen,destino,op):
        enY = origen[1] - destino[1]
        enX = origen[0] - destino[0]
        if enX == 0:
            if enY < 0:
                if op:
                    return 0, -4
                else:
                    return 0,-8
            else:
                if op:
                    return 0, 4
                else:
                    return 0,8

        if enY == 0:
            if enX < 0:
                if op:
                    return -4, 0
                else:
                    return -8,0
            else:
                if op:
                    return 4, 0
                else:
                    return 8,0

        cont = 2
        while cont <= math.fabs(enX) and cont <= math.fabs(enY):
            if enX % cont == 0 and enY % cont == 0:
                enX /= cont
                enY /= cont
                cont = 2
            else:
                cont += 1
        return enX,enY
