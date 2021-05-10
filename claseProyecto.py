 
 
class Proyecto:
    idProyecto=""
    titulo=""
    palabrasClave=""

    def __init__(self, idProyecto="", titulo="", palabrasClave=""):
        self.__idProyecto=idProyecto
        self.__titulo=titulo
        self.__palabrasClave=palabrasClave
    def __str__(self):
        return f"ID del Proyecto:{self.__idProyecto}\nTitulo:{self.__titulo}\nPalabras Clave:{self.__palabrasClave}\n"
    def obtenerID(self):
        return self.__idProyecto
    def __gt__(self,unPuntaje):
        band=None
        if self.__puntaje>unPuntaje.__puntaje: 
             band=True
        else: band=False 
        return band  #Retorna un valor booleano según la comparacion
             
                

    def mostrar(self):
        print (self.__idProyecto,self.__titulo,self.__palabrasClave)
        print ("El puntaje",self.__puntaje)

    def __eq__(self,ID_P):
        band=False
        if self.__idProyecto==ID_P:
            band=True
        return band
