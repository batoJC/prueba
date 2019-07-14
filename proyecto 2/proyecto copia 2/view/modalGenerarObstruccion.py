from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


class modalGenerarObstruccion:

    def __init__(self,app, valores):
        # generar lista de valores
        self.valores = []
        valoresCombo = []
        for valor in valores:
            valoresCombo.append("(" + valor[0] + "," + valor[1] + ")")
            self.valores.append(valor)
        self.res = False
        self.t1 = Toplevel(app)
        self.t1.geometry('400x200+20+20')
        self.t1.title('Generar Obstrucción')
        self.t1.focus_set()
        ## Deshabilita todas las otras ventanas hasta que
        ## esta ventana sea destruida.
        self.t1.grab_set()
        ## Indica que la ventana es de tipo transient, lo que significa
        ## que la ventana aparece al frente del padre.
        self.t1.transient(master=app)

        Label(self.t1, text='Seleccione la tuberia').pack()
        self.tubo = Combobox(self.t1, values=valoresCombo)
        self.tubo.pack()

        ## Crea un widget que permite cerrar la ventana,
        ## para ello indica que el comando a ejecutar es el
        ## metodo destroy de la misma ventana.
        Button(self.t1, text="Generar", bg="green", command=self.generarObstruccion).pack()
        Button(self.t1, text="Cerrar", bg="green", command=self.t1.destroy).pack()

        ## Pausa el mainloop de la ventana de donde se hizo la invocación.
        self.t1.wait_window(self.t1)

    def generarObstruccion(self):
        if self.verificar():
            self.res = True
            self.t1.destroy()

    def verificar(self):
        try:
            tubo = self.tubo.current()
            if tubo > -1:
                self.tubo = self.valores[tubo]
                return True
            else:
                messagebox.showerror(message='Debe seleccionar una tuberia', title="Error")
                return False
        except:
            messagebox.showerror(message='Ocurrio un error', title="Error")
            return False
