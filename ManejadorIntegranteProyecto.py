import csv
from claseIntegranteProyecto import IntegranteProyecto
from claseProyecto import Proyecto

class ManejadorIntegrantesProyecto:
    listaIntegrantes=[]
    def __init__(self):
        self.__listaIntegrantes = []

    def addIntegrantes(self,proyect):
        aux = IntegranteProyecto()
        if type(aux) == type(proyect):
           self.__listaIntegrantes.append(proyect)

    def cargarIntegrantes(self):
         archivo= open ("integrantesProyecto.csv")
         leer= csv.reader(archivo,delimiter=';')
         band = True
         for fila in leer:
             if band:
                " Saltear Cabecera"
                band = False
             else:
                 idProyecto= fila[0]
                 apellidoNombre=fila[1]
                 dni=fila[2]
                 categoriaInvestigacion=fila[3]
                 rol=fila[4]
                 integrante= IntegranteProyecto(idProyecto,apellidoNombre, dni, categoriaInvestigacion,rol)
                 self.addIntegrantes(integrante)
         archivo.close()
    def contar (self,IDProyecto):
        return self.__listaIntegrantes.count(IDProyecto)
    def obtenerDirector(self,idProyecto):
        integrante=IntegranteProyecto()
        for integrante in self.__listaIntegrantes:
            if integrante.obtenerID()==idProyecto:
                if integrante.obtenerRol()=="director":
                                return integrante.obtenerCategoria()
    def obtenerCoDirector(self,idProyecto):
        integrante=IntegranteProyecto()
        for integrante in self.__listaIntegrantes:
            if integrante.obtenerID()==idProyecto:
                if integrante.obtenerRol()=="codirector":
                                return integrante.obtenerCategoria()
    def contarDirector(self,idProyecto):
        integrante=IntegranteProyecto()
        band= False 
        for integrante in self.__listaIntegrantes:
            if integrante.obtenerID()==idProyecto:
                if integrante.obtenerRol()=="director":
                                band=True
        return band
    def contarCodirector(self,idProyecto):
        integrante=IntegranteProyecto()
        band= False 
        for integrante in self.__listaIntegrantes:
            if integrante.obtenerID()==idProyecto:
                if integrante.obtenerRol()=="codirector":
                                band=True
        return band
    
 
   
    def mostrar(self):
             print  (self.__listaIntegrantes[0],self.__listaIntegrantes[1],self.__listaIntegrantes[2],self.__listaIntegrantes[3],self.__listaIntegrantes[4])
