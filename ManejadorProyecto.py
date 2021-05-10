import csv, os
from claseProyecto import Proyecto

class ManejadorProyecto: 
    __listaProyecto=[]   
    def __init__(self):
        self.__listaProyecto = []
    def addProyecto(self,proyect):
        self.__listaProyecto.append(proyect)

    def cargarProyecto(self):

         archivo= open ("proyectos.csv")
         leer= csv.reader(archivo,delimiter=';')
         band = True
         for fila in leer:
             if band:
                ''' Saltear Cabecera'''
                band = False
             else:
               idProyecto= fila[0]
               titulo=fila[1]
               palabrasClave=fila[2]
               proyecto= Proyecto(idProyecto,titulo,palabrasClave)
               self.addProyecto(proyecto)
         archivo.close()
    def calcularPuntaje(self,listaInt,listaProyec):
         listaPuntaj=[]
         listaInt.mostrar()
         listaID=listaProyec.obtenerListaID()
         for ID in listaID:
             puntaje=0
             print ("El ID del Proyecto es:",ID)
             #A
             cantidad_Integrantes=listaInt.contar(ID)

             if cantidad_Integrantes<3:
                 puntaje=puntaje-20
                 print ("Un Proyecto debe tener como minimo 3 integrantes")
             else: puntaje=puntaje+10
             #B
             categDirector=listaInt.obtenerDirector(ID)
             if categDirector != "I" and categDirector !="II":
               puntaje=puntaje-5
               print("El Director del Proyecto debe tener categoría I o II ")
             else: puntaje=puntaje+10
            # print(puntaje)
             #C
             categCoDirector=listaInt.obtenerCoDirector(ID)
          #   print(categCoDirector)
             if categCoDirector =="I" or categCoDirector =="II" or categCoDirector =="III":
                 puntaje=puntaje+10
             else: 
                puntaje=puntaje-5
                print ("El Codirector del Proyecto debe tener como mínimo categoría III")
             
             #D
             existenciaDirector=listaInt.contarDirector(ID)
             if existenciaDirector==False:         
                 print("El Proyecto debe tener un Directo")
             #E
             existenciaCodirector=listaInt.contarCodirector(ID)
             if listaInt.contarCodirector(ID)==False:         
                 print("El Proyecto debe tener un Codirector")
             #F
             if (existenciaCodirector and existenciaDirector)==False:
                 puntaje=puntaje-10
             print("El Proyecto tuvo un puntaje de: ",puntaje)
             print ("----------------------------------")      
             listaPuntaj.append(puntaje)
         self.mejoresPuntajes(listaProyec,listaPuntaj)


    def mejoresPuntajes(self,lista,puntaj):
        unProyecto = Proyecto()
        listaProyectos = ManejadorProyecto()
        listaProyectos = lista.obtenerListaProyectos()
        print(puntaj)
        print('Proyectos ordenados por Puntaje de Mayor a Menor:\n')
        lista.mostrarDatos()
            
            
            
            
    
          
                        
       

    def __gt__(self,unPuntaje):
        band=None
        if self.__puntaje>unPuntaje.__puntaje: 
             band=True
        else: band=False 
        return band  #Retorna un valor booleano según la comparacion
    def obtenerListaID(self):
        listaIDP=[]
        unProyecto = Proyecto()
        for unProyecto in self.__listaProyecto:
            listaIDP.append(unProyecto.obtenerID())
        return listaIDP

    def obtenerListaProyectos(self):
        return self.__listaProyecto


    def mostrarDatos(self):
             print  (self.__listaProyecto[0],self.__listaProyecto[1],self.__listaProyecto[2])
   
    def __str__(self):
        a=""
        unProyecto=Proyecto()
        for unProyecto in self.__listaProyecto:
            a= a+unProyecto.__str__() + '\n'
        return a