
""" — Clase grafo — """

# Importación de módulos
from clases.grafo import *
import random
from interfaz import *
import json
from tkinter import *
from helpers.Keyboard import *

# Uso de diccionarios
librerias = {0 : "Casita", 1 : "Libreria Euler", 2 : "Libreria Gadner", 3 : "Libreria Voronoi", 4 : "Libreria Gauss",
5 : "Libreria Konisberg", 6 : "Libreria Richter", 7 : "Libreria Fibonacci", 8 : "Libreria Fahrenheit", 9 : "Libreria Hilbert",
10 : "Libreria Celsius"}

# Creación de objetos
coyote = Grafo() # Creación del grafo
interfaz = Interfaz(coyote) # Creación de la interfaz

# Rutas archivos json
rutaLibrerias = r'.\data\librerias.json'
rutaRutas = r'.\data\rutas.json'

# Leer json y crear librerías
with open(rutaLibrerias, 'r') as json_file:
    libreriasData = json.loads(json_file.read())
    for l in libreriasData:
        aux = Vertice(**l)
        coyote.ingresarVertice(aux.getNombre(), aux.getX(), aux.getY())

# Leer json y crear rutas
with open(rutaRutas, 'r') as json_file:
    rutasData = json.loads(json_file.read())
    for r in rutasData:
        aux = Arista(**r)
        coyote.ingresarArista(aux.getOrigen(), aux.getDestino(), aux.getPeso())

# Convertir grafo a no dirigido
coyote.noDirigido() 

# Camino bloqueado
def caminoBloqueado():
    origen = "Casita"
    destino = librerias[random.randint(1, 10)] # Genera un camino aleatorio bloqueado
    block = coyote.dijkstra(origen, destino )
    interfaz.crearAristasRecorrido(block,"#FF5300")
    interfaz.xyz22.delete("titulo-recorrido")
    interfaz.getXyz22().create_text(
            450,
            10,
            text="Camino bloqueado",
            anchor="nw",
            font="Roboto 25 bold",
            tags=["titulo-recorrido"],
            fill="#FF5300"
        )
    input()
    alternativa = coyote.caminoBloqueado(origen, destino) # Genera la alternativa mas optima
    interfaz.crearAristasRecorrido(alternativa,"#9E3300")
    interfaz.xyz22.delete("titulo-recorrido")
    interfaz.getXyz22().create_text(
            480,
            10,
            text="Ruta alternativa",
            anchor="nw",
            font="Roboto 25 bold",
            tags=["titulo-recorrido"],
            fill="#9E3300"
        )

    

# Profundidad
def profundidad():
    origen = Keyboard.readIntRangeDefaultErrorMessage("0-Casita\n1-Libreria Euler\n2-Libreria Gadner\n3-Libreria Voronoi\n4-Libreria Gauss\n5-Libreria Konisberg\n6-Libreria Richter\n7-Libreria Fibonacci\n8-Libreria Fahrenheit\n9-Libreria Hilbert\n10-Libreria Celsius\nIngrese El numero del origen:",0,10)
    coyote.recorridoProfundidad(librerias[origen])
    p = coyote.getProfundidad()
    for i in p:
        print(i)
    

# Anchura
def anchura():
    origen = Keyboard.readIntRangeDefaultErrorMessage("0-Casita\n1-Libreria Euler\n2-Libreria Gadner\n3-Libreria Voronoi\n4-Libreria Gauss\n5-Libreria Konisberg\n6-Libreria Richter\n7-Libreria Fibonacci\n8-Libreria Fahrenheit\n9-Libreria Hilbert\n10-Libreria Celsius\nIngrese El numero del origen:",0,10)
    anchura = coyote.aristasAnchura(librerias[origen])
    interfaz.xyz22.delete("titulo-recorrido")
    interfaz.getXyz22().create_text(
            300,
            10,
            text="Anchura desde - " + librerias[origen],
            anchor="nw",
            font="Roboto 25 bold",
            tags=["titulo-recorrido"],
            fill="#00DB8E"
        )
    interfaz.crearAristasRecorrido(anchura, "#00DB8E")
    

# Dijkstra
""" Encuentra la ruta mas corta de entre 2 vertices en específicos"""
def dijkstra():
    origen ="Casita"
    # Verifica la entrada de lita de el numero del destino
    destino = Keyboard.readIntRangeDefaultErrorMessage("0-Casita\n1-Libreria Euler\n2-Libreria Gadner\n3-Libreria Voronoi\n4-Libreria Gauss\n5-Libreria Konisberg\n6-Libreria Richter\n7-Libreria Fibonacci\n8-Libreria Fahrenheit\n9-Libreria Hilbert\n10-Libreria Celsius\nIngrese El numero del destino:",0,10)
    dijkstra = coyote.dijkstra(origen, librerias[destino])
    algoritmo = "Dijkstra" + "  [" + origen + "] ---> ["+ librerias[destino] + "]"  
    interfaz.xyz22.delete("titulo-recorrido")
    interfaz.getXyz22().create_text(
            300,
            10,
            text=algoritmo,
            anchor="nw",
            font="Roboto 25 bold",
            tags=["titulo-recorrido"],
            fill="#8908DB"
        )
    interfaz.crearAristasRecorrido(dijkstra, "#8908DB")

# Prim
""" Encuentra un árbol de expanción mínima a partir de un vertice"""
def prim():
    origen = Keyboard.readIntRangeDefaultErrorMessage("0-Casita\n1-Libreria Euler\n2-Libreria Gadner\n3-Libreria Voronoi\n4-Libreria Gauss\n5-Libreria Konisberg\n6-Libreria Richter\n7-Libreria Fibonacci\n8-Libreria Fahrenheit\n9-Libreria Hilbert\n10-Libreria Celsius\nIngrese El numero del origen:",0,10)
    prim = coyote.prim([],[],[],librerias[origen])
    interfaz.crearAristasRecorrido(prim, "#6EF300")
    interfaz.xyz22.delete("titulo-recorrido")
    interfaz.getXyz22().create_text(
            300,
            10,
            text="prim "+ librerias[origen],
            anchor="nw",
            font="Roboto 25 bold",
            tags=["titulo-recorrido"],
            fill="#6EF300"
        )


# Kruskal
""" Encuentra un árbol de expanción mínima de en un grafo basado en las aristas"""
def kruskal():

    kruskal = coyote.kruskal()
    
    interfaz.xyz22.delete("titulo-recorrido") # Elimina algún titulo de recorrido anterior

    interfaz.getXyz22().create_text(
            525,
            10,
            text="Kruskal",
            anchor="nw",
            font="Roboto 25 bold",
            tags=["titulo-recorrido"],
            fill="#028C9F"
        )
    interfaz.crearAristasRecorrido(kruskal, "#028C9F")

# Boruvka
def boruvka():

    boruvka = coyote.boruvka()

    interfaz.xyz22.delete("titulo-recorrido") # Elimina algún titulo de recorrido anterior

    interfaz.getXyz22().create_text(
            525,
            10,
            text="boruvka",
            anchor="nw",
            font="Roboto 25 bold",
            tags=["titulo-recorrido"],
            fill="#2412DE"
        )
    interfaz.crearAristasRecorrido(boruvka, "#2412DE")

# Función main de ejecución principal
def main ():

    opciones = Menu(interfaz.getVentana())
    
    # Ejecución de los algoritmos
    interfaz.getVentana().config(menu=opciones) # Mostrar ventana del menu
    opciones.add_cascade(label="Camino bloqueado", command= caminoBloqueado)
    opciones.add_cascade(label="Profundidad", command= profundidad)
    opciones.add_cascade(label="Anchura", command= anchura)
    opciones.add_cascade(label="Dijkstra", command= dijkstra)
    opciones.add_cascade(label="Prim", command= prim)
    opciones.add_cascade(label="Kruskal", command= kruskal)
    opciones.add_cascade(label="Boruvka", command= boruvka)

    # Genera carga del grafo
    interfaz.generar() 
    interfaz.crearVertices(coyote.getListaVertices())
    
    mainloop()



# Ejecución de todo el programa
if __name__ == "__main__":
    main()


