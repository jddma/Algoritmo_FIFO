class memoria():

    def __init__(self):
        self.__historial = []
        self.__pagina = []

    def getPagina(self):
        return self.__pagina
    def getUltimoResultado(self):
        return self.__resultado

    def calcularEstadoPagina(self, proceso):
        #si la pagina esta vacia entonces es la primera entrada y retornara fallo
        if len(self.__pagina) == 0:
            self.__pagina.append(proceso)
            self.__historial.insert(0, proceso)
            self.__resultado = False
        elif proceso in self.__pagina:
            """si no es la primera entrada se valida que el proceso entrante ya se encuentre en la pagina
            y si el procesos entrante ya esta en la pagina se pasa a la siguiente sin fallo"""
            self.__resultado = True
        elif len(self.__pagina) < 3:
            #se valida que la pagina no este llena, si no lo esta se agrega el proceso entrante y retorna fallo
            self.__pagina.append(proceso)
            self.__historial.insert(0, proceso)
            self.__resultado = False
        else:
            """si la pagina esta llena se procede a sacar de la pagina el proceso mas viejo  se reempaza con el entrante
            y se retorna fallo"""
            self.__pagina[self.__pagina.index(self.__historial.pop())]=proceso
            #se agrega al historial el nuevo proceso
            self.__historial.insert(0, proceso)
            self.__resultado = False