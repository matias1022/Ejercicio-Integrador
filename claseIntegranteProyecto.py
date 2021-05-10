    
    
class IntegranteProyecto:    
    idProyecto=""
    apellidoNombre=""
    dni=""
    categoriaInvestigacion =""
    rol=""
    
    def __init__(self , idProyecto=" " ,apellidoNombre="",dni="",categoriaInvestigacion="",rol=""):
        self.__idProyecto=idProyecto
        self.__apellidoNombre=apellidoNombre
        self.__dni=dni
        self.__categoriaInvestigacion=categoriaInvestigacion
        self.__rol=rol

    def __str__(self):
        return f"ID del Proyecto:{self.__idProyecto}\nApellido y Nombre:{self.__apellidoNombre}\nDNI:{self.__dni}\nCategoria:{ self.__categoriaInvestigacion}\n Rol:{self.__rol} \n  "
    def __eq__(self,ID_P):
        band=False
        if self.__idProyecto==ID_P:
            band=True
        return band
    def obtenerID(self):
        return self.__idProyecto
    def obtenerCategoria(self):
        return self.__categoriaInvestigacion
    def obtenerRol(self):
        return self.__rol
