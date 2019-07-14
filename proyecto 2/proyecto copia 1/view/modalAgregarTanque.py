from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


class modalAgregarTanque:

    def __init__(self,app):
        self.res = False
        self.t1 = Toplevel(app)
        self.t1.geometry('400x300+20+20')
        self.t1.title('Agregar Tanque')
        self.t1.focus_set()
        ## Deshabilita todas las otras ventanas hasta que
        ## esta ventana sea destruida.
        self.t1.grab_set()
        ## Indica que la ventana es de tipo transient, lo que significa
        ## que la ventana aparece al frente del padre.
        self.t1.transient(master=app)

        Label(self.t1, text='Capacidad en Litros').pack()
        self.capacidad = Entry(self.t1)
        self.capacidad.pack(padx=10, pady=10)

        Label(self.t1, text='Cantidad en Litros').pack()
        self.cantidad = Entry(self.t1)
        self.cantidad.pack(padx=10, pady=10)

        Label(self.t1, text='Fila').pack()
        self.fila = Entry(self.t1)
        self.fila.pack(padx=10, pady=10)

        Label(self.t1, text='Columna').pack()
        self.columna = Entry(self.t1)
        self.columna.pack(padx=10, pady=10)


        ## Crea un widget que permite cerrar la ventana,
        ## para ello indica que el comando a ejecutar es el
        ## metodo destroy de la misma ventana.
        Button(self.t1, text="Agregar", bg="green", command=self.agregarTanque).pack()
        Button(self.t1, text="Cerrar", bg="green", command=self.t1.destroy).pack()

        ## Pausa el mainloop de la ventana de donde se hizo la invocación.
        self.t1.wait_window(self.t1)

    def agregarTanque(self):
        if self.verificar():
            self.res = True
            self.t1.destroy()

    def verificar(self):
        try:
            capacidad = int(self.capacidad.get())
            cantidad = int(self.cantidad.get())
            fila = int(self.fila.get())
            columna = int(self.columna.get())
            if capacidad >=  0 and cantidad >= 0 and 0 < fila < 12 and 0 < columna < 20:
                self.capacidad = capacidad
                self.cantidad = cantidad
                self.fila = fila
                self.columna = columna
                return True
            else:
                messagebox.showerror(message='Los valores deben ser números Positivos (filas entre 1 y 11, columnas entre 1 y 19)', title="Error")
                return False

        except ValueError:
            messagebox.showerror(message='Los valores deben ser números', title="Error")
            return False
