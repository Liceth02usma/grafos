""" — Mirar bien canvas — """

# Importación de módulos
from tkinter import *
import tkinter as tk

class Interfaz:

    # Constructor
    def __init__(self, grafo):

        self.grafo = grafo # Grafo
        self.ventana = Tk() # Ventana
        self.ventana.geometry("1200x650") # Tamaño de la ventana
        self.ventana.title("Ciudad coyote") # Nombre del Proyecto
        self.ventana.resizable(width=False, height=False) # no renderización de la ventana 
        self.xyz22 = Canvas(self.ventana) # Manejo de la  superficie  
        self.xyz22.pack(fill=BOTH, expand=True) # Posicionamiento
        self.urlFondo = "./recursos/fondo.png"
        self.agregarFondo()
        self.imagenes = []

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""
    def getVentana(self):
        return self.ventana
    
    def getXyz22(self):
        return  self.xyz22

    def generar(self):
        self.xyz22.delete("linea")
        self.crearAristas()

    def agregarFondo(self):
        """Pone una imagen de fondo en la ventana principal."""
        
        self.imagenFondo = PhotoImage(file=self.urlFondo)
        self.xyz22.create_image(0, 0, image=self.imagenFondo, anchor="nw")
        self.xyz22.pack(fill=BOTH, expand=True)
    
    def crearAristas(self):
        for arista in self.grafo.listaAristas:
            origen = self.grafo.obtenerVertice(arista.getOrigen(), self.grafo.getListaVertices())
            destino = self.grafo.obtenerVertice(arista.getDestino(), self.grafo.getListaVertices())
            self.crearArista(
                origen.getX(),
                origen.getY(),
                destino.getX(),
                destino.getY(),
                arista.getPeso()
                )

    def crearAristasRecorrido(self, recorrido, color):
        self.xyz22.delete("recorrido")

        for arista in recorrido:
            origen = self.grafo.obtenerVertice(arista.getOrigen(), self.grafo.getListaVertices())
            destino = self.grafo.obtenerVertice(arista.getDestino(), self.grafo.getListaVertices())
            self.crearArista(
                origen.getX(),
                origen.getY(),
                destino.getX(),
                destino.getY(),
                0,
                color,
                "recorrido",
                6,
            )
    
    def crearArista(self, x1, y1, x2, y2, peso, color="#3c3c3c", tag="linea", grosor=3):
        """Crea una nueva linea entre dos vertices."""

        self.xyz22.create_line(
            x1, y1 + 25, x2, y2 + 25, fill=color, width=grosor, tags=[tag]
        )
    
        if peso > 0:
            self.xyz22.create_text(
                (x1 + x2) / 2,
                ((y1 + 25 + y2 + 25) / 2) - 10,
                text=peso,
                font="Roboto 20 italic",
                tags=["peso"],
            )

    
    def crearVertices(self, listaVertices):
        for vertice in listaVertices:
            self.crearVertice(
                vertice.getX(), vertice.getY(), vertice.getNombre(), vertice.getImagen()
            )
    
    def crearVertice(self, x, y, nombre, imagen):
        """Crea una nueva imagen de un planeta en el canvas."""
        # urlImagen = "./images/casita.png"
        self.imagenes.append(None)
        self.imagenes[len(self.imagenes) - 1] = PhotoImage(file=imagen)
        idImg = self.xyz22.create_image(
            x, y, image=self.imagenes[len(self.imagenes) - 1], anchor="center"
        )
        self.xyz22.create_text(x + 5, y - 35, text=nombre, font="Cascadia 19 roman", fill="#E74C3C")
        return idImg


    def pintarRecorrido(self):
        self.xyz22.delete("linea")
        self.xyz22.delete("recorrido")
        for arista in self.grafo.listaAristas:
            origen = self.grafo.obtenerVertice(arista.getOrigen(), self.grafo.getListaVertices())
            destino = self.grafo.obtenerVertice(arista.getDestino(), self.grafo.getListaVertices())
            print("oe",arista.getColor())
            self.crearArista(
                origen.getX(),
                origen.getY(),
                destino.getX(),
                destino.getY(),
                arista.getPeso(),
                arista.getColor(),
                "recorrido",
                6,

                )