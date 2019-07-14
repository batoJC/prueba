from tkinter import *
from tkinter import messagebox

class modalAgregarTubo:

    def __init__(self,app):
        self.res = False
        self.t1 = Toplevel(app)
        self.t1.geometry('400x300+20+20')
        self.t1.title('Agregar Tubo')
        self.t1.focus_set()
        ## Deshabilita todas las otras ventanas hasta que
        ## esta ventana sea destruida.
        self.t1.grab_set()
        ## Indica que la ventana es de tipo transient, lo que significa
        ## que la ventana aparece al frente del padre.
        self.t1.transient(master=app)

        Label(self.t1, text='Capacidad en litros').pack()
        self.capacidad = Entry(self.t1)
        self.capacidad.pack(padx=10, pady=10)

        Label(self.t1, text='Origen').pack()
        self.origen = Entry(self.t1)
        self.origen.pack(padx=10, pady=10)

        Label(self.t1, text='Destino').pack()
        self.destino = Entry(self.t1)
        self.destino.pack(padx=10, pady=10)


        ## Crea un widget que permite cerrar la ventana,
        ## para ello indica que el comando a ejecutar es el
        ## metodo destroy de la misma ventana.
        Button(self.t1, text="Agregar", bg="green", command=self.agregarTubo).pack()
        Button(self.t1, text="Cerrar", bg="green", command=self.t1.destroy).pack()

        ## Pausa el mainloop de la ventana de donde se hizo la invocación.
        self.t1.wait_window(self.t1)

    def agregarTubo(self):
        if self.verificar():
            self.res = True
            self.t1.destroy()

    def verificar(self):
        try:
            capacidad = int(self.capacidad.get())
            origen = self.origen.get()
            destino = self.destino.get()

            if capacidad > 0:
                self.capacidad = capacidad
                if origen != '' and destino != '':
                    self.origen = origen
                    self.destino = destino
                    return True
            else:
                messagebox.showerror(message='Los valores deben ser números Positivos', title="Error")
                return False

        except ValueError:
            messagebox.showerror(message='Los valores deben ser números', title="Error")
            return False
