from modelo.memoria import memoria


class inicio_controlador():

    def instanciarMemoria(self):
        self.__ram = memoria()

    def destruirMemoria(self):
        del self.__ram

    def getUltimoResultado(self):
        return self.__ram.getUltimoResultado()

    def calcularEstadoPagina(self, proceso):
        self.__ram.calcularEstadoPagina(proceso)
        result = self.__ram.getPagina()
        return result