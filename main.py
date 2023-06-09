
""" — Clase grafo — """

# Importación de módulos
from clases.grafo import *
import random
from interfaz import *
import json
from tkinter import simpledialog 
from tkinter import *
from helpers.Keyboard import *

# Uso de diccionarios
librerias = {0 : "Casita", 1 : "Libreria Euler", 2 : "Libreria Gadner", 3 : "Libreria Voronoi", 4 : "Libreria Gauss",
5 : "Libreria Konisberg", 6 : "Libreria Richter", 7 : "Libreria Fibonacci", 8 : "Libreria Fahrenheit", 9 : "Libreria Hilbert",
10 : "Libreria Celsius"}

# Creación de objetos
aeropuertos = Grafo() # Creación del grafo
interfaz = Interfaz(aeropuertos) # Creación de la interfaz



# Rutas archivos json
rutaLibrerias = r'.\data\librerias.json'
rutaRutas = r'.\data\rutas.json'

# Leer json y crear librerías
with open(rutaLibrerias, 'r') as json_file:
    libreriasData = json.loads(json_file.read())
    for l in libreriasData:
        aux = Vertice(**l)
        aeropuertos.ingresarVertice(aux.getNombre(), aux.getX(), aux.getY())

# Leer json y crear rutas
with open(rutaRutas, 'r') as json_file:
    rutasData = json.loads(json_file.read())
    for r in rutasData:
        aux = Arista(**r)
        aeropuertos.ingresarArista(aux.getOrigen(), aux.getDestino(), aux.getPeso())

# Convertir grafo a no dirigido
aeropuertos.noDirigido() 

# Camino bloqueado
def caminoBloqueado():
    origen = "Casita"
    destino = librerias[random.randint(1, 10)] # Genera un camino aleatorio bloqueado
    block = aeropuertos.dijkstra(origen, destino )
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
    alternativa = aeropuertos.caminoBloqueado(origen, destino) # Genera la alternativa mas optima
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
    aeropuertos.recorridoProfundidad(librerias[origen])
    p = aeropuertos.getProfundidad()
    for i in p:
        print(i)
    

# Anchura
def anchura():
    origen = Keyboard.readIntRangeDefaultErrorMessage("0-Casita\n1-Libreria Euler\n2-Libreria Gadner\n3-Libreria Voronoi\n4-Libreria Gauss\n5-Libreria Konisberg\n6-Libreria Richter\n7-Libreria Fibonacci\n8-Libreria Fahrenheit\n9-Libreria Hilbert\n10-Libreria Celsius\nIngrese El numero del origen:",0,10)
    anchura = aeropuertos.aristasAnchura(librerias[origen])
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
    



""" Agrega vertices"""
def agregar_vertice(event):
    if interfaz.ok_agregar.get():
        x = event.x
        y = event.y
        nombre = simpledialog.askstring("Agregar Vertice", "Ingresa el nombre del aeropuerto")
        aeropuertos.ingresarVertice(nombre, x, y)
        interfaz.crearVertices(aeropuertos.listaVertices)
        interfaz.ok_agregar.set(False)

        interfaz.getVentana().update() 

    elif interfaz.ok_agregarV.get():
        id_imagen = event.widget.find_withtag(tk.CURRENT)[0]
        vertice = None
        for i in aeropuertos.listaVertices:
            if i.Id == id_imagen:
                vertice = i
        if vertice != None:
            interfaz.lista.append(vertice)
        if len(interfaz.lista)==2:
            peso = int(simpledialog.askstring("Agregar Arista", "Ingrese la distancia"))
            aeropuertos.ingresarArista(interfaz.lista[0].nombre, interfaz.lista[1].nombre, peso)
            interfaz.crearArista(interfaz.lista[0].x,interfaz.lista[0].y,interfaz.lista[1].x, interfaz.lista[1].y, peso)
            
            interfaz.lista.clear()
            interfaz.ok_agregarV.set(False)
            interfaz.getVentana().update() 
    
""" Agrega vertices"""
def cambiar():
    interfaz.ok_agregar.set(True)
    
def cambiar_valor():
    interfaz.ok_agregarV.set(True)


# Dijkstra
""" Encuentra la ruta mas corta de entre 2 vertices en específicos"""
def dijkstra():
    origen ="Casita"
    # Verifica la entrada de lita de el numero del destino
    destino = Keyboard.readIntRangeDefaultErrorMessage("0-Casita\n1-Libreria Euler\n2-Libreria Gadner\n3-Libreria Voronoi\n4-Libreria Gauss\n5-Libreria Konisberg\n6-Libreria Richter\n7-Libreria Fibonacci\n8-Libreria Fahrenheit\n9-Libreria Hilbert\n10-Libreria Celsius\nIngrese El numero del destino:",0,10)
    dijkstra = aeropuertos.dijkstra(origen, librerias[destino])
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
    prim = aeropuertos.prim([],[],[],librerias[origen])
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

    kruskal = aeropuertos.kruskal()
    
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

    boruvka = aeropuertos.boruvka()

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
    # opciones.add_cascade(label="Camino bloqueado", command= caminoBloqueado)
    # opciones.add_cascade(label="Profundidad", command= profundidad)
    # opciones.add_cascade(label="Anchura", command= anchura)
    interfaz.getVentana().bind("<Button-1>", agregar_vertice)
    opciones.add_cascade(label="Agregar Vertice", command= cambiar)
    opciones.add_cascade(label="Agregar Arista", command= cambiar_valor)
    opciones.add_cascade(label="Dijkstra", command= dijkstra)
    # opciones.add_cascade(label="Prim", command= prim)
    # opciones.add_cascade(label="Kruskal", command= kruskal)
    # opciones.add_cascade(label="Boruvka", command= boruvka)

    # Genera carga del grafo
    interfaz.generar() 
    interfaz.crearVertices(aeropuertos.getListaVertices())
    
    mainloop()



# Ejecución de todo el programa
if __name__ == "__main__":
    main()


