
""" — Clase grafo — """

# Importación de módulos
from clases.grafo import *
import random
from interfaz import *
import json
from tkinter import simpledialog, messagebox 
from tkinter import *
from helpers.Keyboard import *


# Creación de objetos
aeropuertos = Grafo() # Creación del grafo
interfaz = Interfaz(aeropuertos) # Creación de la interfaz



# Rutas archivos json
rutaLibrerias = r'.\data\aeropuertos.json'
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
        aux = Arista(r["origen"],r["destino"],r["peso"],r["tiempo"])
        aeropuertos.ingresarArista(aux.getOrigen(), aux.getDestino(), aux.getPeso(), aux.tiempo)


def actualizar_data_ruta():
    with open(rutaRutas, 'w') as archivo:
        json.dump(aeropuertos.listaAristas, archivo, default=aeropuertos.serializar_objeto, indent=4)
        
def actualizar_data_aeropuertos():
    with open(rutaLibrerias, 'w') as archivo:
        json.dump(aeropuertos.listaVertices, archivo, default=aeropuertos.serializar_objeto2, indent=4)
    
# Convertir grafo a no dirigido
aeropuertos.noDirigido() 
print(len(aeropuertos.listaVertices))
# Camino bloqueado

    

# Profundidad 



""" Agrega vertices"""
def agregar_vertice(event):
    if interfaz.ok_agregar.get():
        x = event.x
        y = event.y
        nombre = simpledialog.askstring("Agregar Aeropuerto", "Ingresa el nombre del aeropuerto")
        aeropuertos.ingresarVertice(nombre, x, y)
        interfaz.crearVertices(aeropuertos.listaVertices)
        interfaz.ok_agregar.set(False)
        actualizar_data_aeropuertos()
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
            peso = int(simpledialog.askstring("Agregar Ruta", "Ingrese la distancia"))
            tiempo = int(simpledialog.askstring("Agregar Ruta", "Ingrese la tiempo"))
            aeropuertos.ingresarArista(interfaz.lista[0].nombre, interfaz.lista[1].nombre, peso, tiempo)
            interfaz.crearArista(interfaz.lista[0].x,interfaz.lista[0].y,interfaz.lista[1].x, interfaz.lista[1].y, peso,f"{peso}km-{tiempo}m")
            actualizar_data_ruta()
            interfaz.lista.clear()
            interfaz.ok_agregarV.set(False)
            interfaz.crearVertices(aeropuertos.listaVertices)
            interfaz.getVentana().update() 
    elif interfaz.ok_agregar_edit.get():
        id = event.widget.find_withtag(tk.CURRENT)[0]
        editar_valor(id)
        interfaz.ok_agregar_edit.set(False)
    
    
""" Agrega vertices"""
def cambiar():
    interfaz.ok_agregar.set(True)
    
def cambiar_valor():
    interfaz.ok_agregarV.set(True)
    
def cambiar_editar():
    interfaz.ok_agregar_edit.set(True)

    
    
def opcion(indice,indice2):
    value = None
    while True:
        opcion = int(simpledialog.askstring("Actualizar", "Ingrese el valor correspondiente de lo que desee actualizar:\n 1.Distancia\n 2.Tiempo\n 4.Salir"))
        if opcion >= 1 and opcion <=4:
            if opcion == 1:
                while True:
                    try:
                        value = int(simpledialog.askstring("Distancia", "Ingrese la distancia"))
                        break
                    except:
                        messagebox.showinfo("¡Error!","El valor no es correcto")
                
                aeropuertos.listaAristas[indice].peso = value
                aeropuertos.listaAristas[indice].distancia = value
                aeropuertos.listaAristas[indice2].peso = value
                aeropuertos.listaAristas[indice2].distancia = value
            elif opcion == 2:
                while True:
                    try:
                        value = int(simpledialog.askstring("Tiempo", "Ingrese el tiempo"))
                        break
                    except:
                        messagebox.showinfo("¡Error!","El valor no es correcto")
                aeropuertos.listaAristas[indice].tiempo = value
                aeropuertos.listaAristas[indice2].tiempo = value
            elif opcion == 4:
                break
    
def editar_valor(id):
    arista = None
    for i in aeropuertos.listaAristas:
        if i.Id == id:
            arista = i
    origen = arista.origen
    destino = arista.destino
    arista = aeropuertos.obtenerArista(origen, destino, aeropuertos.listaAristas)
    arista2 = aeropuertos.obtenerArista(destino, origen, aeropuertos.listaAristas)
    indice = aeropuertos.listaAristas.index(arista)
    indice2 = aeropuertos.listaAristas.index(arista2)
    value = messagebox.askquestion("Confirmar", f"¿Desea actualizar la ruta?:\n {origen} - {destino}")
    if value != "No":
        opcion(indice,indice2)
        interfaz.xyz22.delete("peso")
        interfaz.crearAristas()
        interfaz.crearVertices(aeropuertos.listaVertices)
        interfaz.getVentana().update()
        actualizar_data_ruta()


# Dijkstra
""" Encuentra la ruta mas corta de entre 2 vertices en específicos"""
def dijkstra():
    origen ="Casita"
    # Verifica la entrada de lita de el numero del destino
    destino = Keyboard.readIntRangeDefaultErrorMessage("0-Casita\n1-Libreria Euler\n2-Libreria Gadner\n3-Libreria Voronoi\n4-Libreria Gauss\n5-Libreria Konisberg\n6-Libreria Richter\n7-Libreria Fibonacci\n8-Libreria Fahrenheit\n9-Libreria Hilbert\n10-Libreria Celsius\nIngrese El numero del destino:",0,10)
    dijkstra = aeropuertos.dijkstra(origen, librerias[destino])
    for i in dijkstra:
        print(i.peso, i.origen, i.destino)
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
    opciones.add_cascade(label="Agregar Aeropuerto", command= cambiar)
    opciones.add_cascade(label="Agregar Ruta", command= cambiar_valor)
    opciones.add_cascade(label="Editar Ruta", command= cambiar_editar)
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


