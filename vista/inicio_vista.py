import tkinter as tk
from tkinter import messagebox as MessageBox

from controlador.inicio_controlador import inicio_controlador


class inicio_vista(tk.Frame):

    def __init__(self):
        super().__init__(None)

        #instanciar el controlador
        self.__ctrl = inicio_controlador()

        #configuración de la centana
        self.master.title("Simulador algoritmo de gestión de memoria FIFO")
        self.master.resizable(False, False)

        #instancia los Entry de los procesos y lo coloca en la interfaz
        self.__procesos = []
        for i in range(12):
            self.__procesos.append(tk.Entry(width = 3))
        for i in range(len(self.__procesos)):
            self.__procesos[i].grid(row = 0, column = i)

        # atrapar, guardar y colocar el boron de inico de la simulación
        self.__btnInicio = tk.Button(text="Iniciar", width=14, command=self.__iniciarSimulacion)

        self.__btnInicio.grid(row=0, column=12)

        #instanciar las etiquetas de los estados de la memoria
        self.__lbEstadoMemoria = []
        for i in range(12):
            self.__lbEstadoMemoria.append([tk.Label(text = "  ", borderwidth = 2, relief="groove", width = 10), tk.Label(text = "   ", borderwidth = 2, relief="groove", width = 10), tk.Label(text = "   ", borderwidth = 2, relief="groove", width = 10)])
        for i in range(12):
            self.__lbEstadoMemoria[i][0].grid(row = 1, column = i)
            self.__lbEstadoMemoria[i][1].grid(row = 2, column = i)
            self.__lbEstadoMemoria[i][2].grid(row = 3, column = i)

        #instancia las etiquetas de los resultados de cada etapa
        self.__lbResultados = []
        for i in range(12):
            self.__lbResultados.append(tk.Label(text = "_", borderwidth = 2, relief="groove", width = 10))
            self.__lbResultados[i].grid(row = 4, column = i)

        #fin del sideño de la interfaz
        self.master.mainloop()

    def __deshabilitarInputs(self):
        for i in range(len(self.__procesos)):
            self.__procesos[i].config(state = "disabled")
        self.__btnInicio.config(state = "disabled")

    def __habilitarInputs(self):
        for i in range(len(self.__procesos)):
            self.__procesos[i].config(state = "normal")
        self.__btnInicio.config(state="normal")

    def __iniciarProceso(self, procesos_solicitados):
        #hace que el controlador instancie la clase memoria que solo existira mientras se simule un proceso
        self.__ctrl.instanciarMemoria()

        #recorre los procesos ingresados por el usuario para procesarlos uno a la vez
        for i in range(len(procesos_solicitados)):
            #llama al metodo que realiza el calculo de la pagina
            estado_pagina = self.__ctrl.calcularEstadoPagina(procesos_solicitados[i])
            print(estado_pagina)
            #el try es para que el programa no falle cuando hallan espacios vacios en la pagina
            try:
                self.__lbEstadoMemoria[i][0]["text"] = (str(estado_pagina[0]))
                self.__lbEstadoMemoria[i][1]["text"] = (str(estado_pagina[1]))
                self.__lbEstadoMemoria[i][2]["text"] = (str(estado_pagina[2]))
            except:
                pass
            #coloca el resultado de la operacion de la pagina
            if not self.__ctrl.getUltimoResultado():
                self.__lbResultados[i]["text"]="F"
            else:
                self.__lbResultados[i]["text"] = "_"
        self.__ctrl.destruirMemoria()

    def __iniciarSimulacion(self):
        print("Iniciando")
        self.__deshabilitarInputs()

        #obtiene los datos de los inputs y verifica si todos estan llenos
        procesos_solicitados = []
        validez = True
        for i in self.__procesos:
            if i.get() == "":
                MessageBox.showwarning("Campos en blanco", "Llene todos los campos gran idiota")
                validez = False
                break
            else:
                procesos_solicitados.append(i.get())
        if validez:
            self.__iniciarProceso(procesos_solicitados)
        #habilita los inputs
        self.__habilitarInputs()

if __name__ == "__main__":
    inicio_vista()