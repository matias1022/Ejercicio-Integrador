from ManejadorProyecto import ManejadorProyecto
from claseProyecto import Proyecto
from ManejadorIntegranteProyecto import ManejadorIntegrantesProyecto
from claseIntegranteProyecto import IntegranteProyecto

if __name__ == '__main__':

    listaP= ManejadorProyecto()
    listaP.cargarProyecto()
    listaI=ManejadorIntegrantesProyecto()
    listaI.cargarIntegrantes()
    listaP.calcularPuntaje(listaI, listaP)