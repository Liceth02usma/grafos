"""— Clase grafo —"""

#  Importación de módulos
from copy import copy #para realizar copias de objetos
from clases.arista import *
from clases.vertice import *

class Grafo:

   # Constructor
   def __init__(self):
      self.listaVertices = []
      self.listaAristas = []
      self.profundidad = []
      self.anchura = []
   
   """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""
   
   # Set - Get | lista de vertices
   def getListaVertices(self):
      return self.listaVertices

   def setListaVertices(self, listaVertices):
      self.listaVertices = listaVertices

   # Set - Get | lista de aristas
   def getListaAristas(self):
      return self.listaAristas

   def setListaAristas(self, listaAristas):
      self.listaAristas = listaAristas

   # Set - Get | recorrido profundidad
   def getProfundidad(self):
      return self.profundidad

   def setProfundidad(self, profundidad):
      self.profundidad = profundidad

   # Set - Get | recorrido anchura
   def getAnchura(self):
      return self.anchura

   def setAnchura(self,anchura):
      self.anchura = anchura

   """—————————————————————————————————————————FUNCIONES VERTICE————————————————————————————————————————————————"""
   # Ingresar vértice
   def ingresarVertice(self, nombre, x, y):
      if not self.existeVertice(nombre, self.listaVertices):
            self.listaVertices.append(Vertice(nombre, x, y))

   # Existe vértice
   def existeVertice(self, nombre, listaVertices):
      for i in listaVertices:
         if nombre == i.getNombre():
            return True
      return False

   # Obtener vértice
   def obtenerVertice(self, origen, lista):
      for i in lista:
         if origen == i.getNombre():
            return i

   """—————————————————————————————————————————FUNCIONES ARISTA—————————————————————————————————————————————————"""

   # Ingresar arista
   def ingresarArista(self, origen, destino, peso):
      if not self.existeArista(origen, destino, self.listaAristas):
         if self.existeVertice(origen, self.listaVertices) and self.existeVertice(destino, self.listaVertices):
            self.listaAristas.append(Arista(origen, destino, peso))
            self.obtenerVertice(origen, self.listaVertices).getListaAdyacentes().append(destino)

   # Existe arista
   def existeArista(self, origen, destino, lista):
      for i in lista:
         if origen == i.getOrigen() and destino == i.getDestino():
            return True
      return False     
   
   # Obtener Arista
   def obtenerArista(self, origen, destino, lista):
      for i in lista:
         if origen == i.getOrigen() and destino == i.getDestino():
            return i
   
   # Obtener arista de menor peso
   def obtenerAristaMenor(self, aristas):
      menor = aristas[0]
      for a in aristas:  
         if a.getPeso() < menor.getPeso():
            menor = a
      return menor
   
   def eliminarArista(self, origen, destino):
      verticeOrigen = self.obtenerVertice(origen, self.listaVertices)
      aristaOrigen = self.obtenerArista(origen, destino, self.listaAristas)
      if aristaOrigen:
         verticeOrigen.getListaAdyacentes().pop(verticeOrigen.getListaAdyacentes().index(destino))
         self.listaAristas.pop(self.listaAristas.index(aristaOrigen))

      verticeDestino = self.obtenerVertice(destino, self.listaVertices)
      aristaDestino = self.obtenerArista(destino, origen, self.listaAristas)
      if aristaDestino:
         verticeDestino.getListaAdyacentes().pop(verticeDestino.getListaAdyacentes().index(origen))
         self.listaAristas.pop(self.listaAristas.index(aristaDestino))
      
   """—————————————————————————————————————————————FUNCTIONS————————————————————————————————————————————————————————"""           

   # Convertir dirigido a no dirigido
   def noDirigido(self):
      lista = copy(self.listaAristas)
      for i in lista:
         crear = True
         for j in lista:
            if i.getOrigen() == j.getDestino() and i.getDestino() == j.getOrigen():
               crear = False
               break
         if crear:
            self.ingresarArista(i.getDestino(), i.getOrigen(), i.getPeso())
   
   # Convertir no dirigido a dirigido
   def dirigido(self):
      lista = copy(self.listaAristas)
      for i in lista:
         arista = False
         for j in lista:
            
            if i.getOrigen() == j.getDestino() and i.getDestino() == j.getOrigen():
               arista = j
               break
         if arista:
            lista.pop(lista.index(arista))
            vertice = self.obtenerVertice(arista.getOrigen(), self.listaVertices)
            vertice.getListaAdyacentes().pop(vertice.getListaAdyacentes().index(arista.getDestino()))

      self.setListaAristas(lista)

   # Recorrido en profundidad
   def recorridoProfundidad(self, nombre):
      if nombre in self.profundidad:
         return
      vertice = self.obtenerVertice(nombre, self.listaVertices)
      if vertice != None:
         self.profundidad.append(vertice.getNombre())
         for dato in vertice.getListaAdyacentes():
            self.recorridoProfundidad(dato)

   
   # Recorrido en anchura
   def recorridoAnchura(self, nombre):
      visitados = []
      cola =  []
      cola.append(nombre)
      for i in self.listaVertices:
         visitados.append(False)
      self.ra(cola, visitados)
   

   def recorridoProfundidad(self, dato):
      if dato in self.profundidad:
         return
      else:
         vertice = self.obtenerVertice(dato,self.listaVertices)
         if vertice != None:
            self.profundidad.append(vertice.getNombre())
            for dato in vertice.getListaAdyacentes():
               self.recorridoProfundidad(dato)

      return self.profundidad

   def ra(self, cola, visitados):
      if len(cola) == 0:
         return
      vertice = self.obtenerVertice(cola.pop(0), self.listaVertices)
      self.anchura.append(vertice.getNombre())
      visitados[self.listaVertices.index(vertice)] = True
      for a in vertice.getListaAdyacentes():
         if not (a in cola) and not (visitados[self.listaVertices.index(self.obtenerVertice(a, self.listaVertices))]):
            cola.append(a)
      self.ra(cola, visitados)

   # Algoritmo de kruskal
   def kruskal(self):
      aristas = copy(self.listaAristas)
      # Eliminar aristas repetidas
      for i in aristas:
         arista = False
         for j in aristas:
            if i.getOrigen() == j.getDestino() and i.getDestino() == j.getOrigen():
               arista = j
               break
         if arista:
            aristas.pop(aristas.index(arista))
      # Vertices visitados
      visitados = []  
      for v in self.listaVertices:
         visitados.append(False)
      return self.ordenarKruskal(visitados, aristas, [])

   def ordenarKruskal(self, visitados, aristas, recorrido):
      # Retornar cuando el árbol de expanción minima este formado
      if len(recorrido) == len(self.listaVertices)-1:
         return recorrido
      # Eliminar aristas que formen ciclos
      for vis in aristas:  
         if visitados[self.listaVertices.index(self.obtenerVertice(vis.getDestino(), self.listaVertices))] == True:
            aristas.pop(aristas.index(vis))
      # Obtener arista de menor peso
      menor = self.obtenerAristaMenor(aristas) 
      recorrido.append(aristas.pop(aristas.index(menor)))
      return self.ordenarKruskal(visitados, aristas, recorrido)

   # Dijkstra
   def dijkstra(self, origen, destino):
      verticesAux = []
      verticesD = []
      caminos = self.ordenarDijkstra(origen, verticesAux)
      self.rutas(verticesD, verticesAux, destino, origen)
      aristas = []
      for i in range(len(verticesD)-1):
         aristas.append(self.obtenerArista(verticesD[i],verticesD[i+1], self.listaAristas))
      return aristas

   def ordenarDijkstra(self, origen, verticesAux):
      visitados = []  # lista de visitados
      caminos = []  # recorrido final

      for v in self.listaVertices:  # iniciar los valores en infinito
         caminos.append(float("inf"))
         visitados.append(False)
         verticesAux.append(None)
         if v.getNombre() == origen:
            caminos[self.listaVertices.index(v)] = 0
            verticesAux[self.listaVertices.index(v)] = v.getNombre()

      while not self.todosVisitados(visitados):
            menorAux = self.menorNoVisitado(caminos, visitados)  # obtiene el menor no visitado
            if menorAux == None:
               break
            indice = self.listaVertices.index(menorAux)  # indice del menor no marcado
            visitados[indice] = True
            valorActual = caminos[indice]

            for adyacencia in menorAux.getListaAdyacentes():
               indiceNuevo = self.listaVertices.index(self.obtenerVertice(adyacencia, self.listaVertices))
               arista = self.verificarArista(menorAux.getNombre(), adyacencia)
               if caminos[indiceNuevo] > valorActual + arista.getPeso():
                  caminos[indiceNuevo] = valorActual + arista.getPeso()
                  verticesAux[indiceNuevo] = self.listaVertices[indice].getNombre()

      return caminos

   def verificarArista(self, origen, destino):
      for i in range(len(self.listaAristas)):
         if origen == self.listaAristas[i].getOrigen() and destino == self.listaAristas[i].getDestino():
               return self.listaAristas[i]
      return None

   def todosVisitados(self, visitados):
      for vertice in visitados:
         if vertice == False:
            return False

      return True

   def menorNoVisitado(self, caminos, visitados):
      verticeMenor = None
      caminosAux = sorted(caminos)  # de menor a mayor

      copiaCaminos = copy(caminos)
      bandera = True
      cont = 0

      while bandera:
         menor = caminosAux[cont]

         if visitados[copiaCaminos.index(menor)] == False:
            verticeMenor = self.listaVertices[copiaCaminos.index(menor)]
            bandera = False

         else:
            copiaCaminos[copiaCaminos.index(menor)] = "x"
            cont += 1

      return verticeMenor

   def rutas(self, verticesD, verticesAux, destino, origen):
      verticeDestino = self.obtenerVertice(destino, self.listaVertices)
      indice = self.listaVertices.index(verticeDestino)

      if verticesAux[indice] == None:
         print("No hay camino entre: ", (origen, destino))
         return
      aux = destino

      while aux != origen:
         verticeDestino = self.obtenerVertice(aux, self.listaVertices)
         indice = self.listaVertices.index(verticeDestino)
         verticesD.insert(0, aux)
         aux = verticesAux[indice]
      verticesD.insert(0, aux)

   # Prim
   def prim(self, visitados, aristas, recorrido, origen):
      if len(self.listaVertices)-1 == len(visitados):
         return recorrido
      # Obtener vertice 
      vertice = self.obtenerVertice(origen, self.listaVertices)
      visitados.append(vertice)

      # Obtener aristas candidatas
      for i in vertice.getListaAdyacentes():
         aristas.append(self.obtenerArista(origen, i, self.listaAristas))

      aux = []
      # Eliminar aristas que formen ciclos
      for a in aristas:
         cliclo = False
         for v in visitados:
            if a.getDestino() == v.getNombre():
               cliclo = True
               break
         if not cliclo:
            aux.append(a)
      aristas = aux
      # Obtener arista menor
      menor = self.obtenerAristaMenor(aristas)
      recorrido.append(aristas.pop(aristas.index(menor)))

      return self.prim(visitados, aristas, recorrido, menor.getDestino())

   # Bloquea una ruta en especifico y busca segunda ruta mas optima
   def caminoBloqueado(self, origen, destino):
      lista = self.dijkstra(origen, destino)  
      for i in lista:
         self.eliminarArista(i.getOrigen(), i.getDestino())
      block = self.dijkstra(origen, destino)
      for i in lista:
         self.ingresarArista(i.getOrigen(), i.getDestino(), i.getPeso())
         
      return block
   
   # Boruvka
   def boruvka(self):   

      vertices = [] # Lista total de vertices
      aristas = [] # Lista de lista de aristas adyacentes
      recorrido = []

      # Inicializar listas
      for v in self.listaVertices:
         # Inicializar vertices con conjunto de vertices 
         conjuntoVertice= []
         conjuntoVertice.append(v)
         vertices.append(conjuntoVertice)
         # Lista de conjuntos de menores
         # recorrido.append([]) 
         # Inicializar listas de aristas
         listaAristas = []
         for adyacente in v.getListaAdyacentes():
            listaAristas.append(self.obtenerArista(v.getNombre(), adyacente, self.listaAristas))
         aristas.append(listaAristas)
   
   def ordenarBoruvka(self, vertices, aristas, recorrido):
      if len(recorrido) == 10:
         return recorrido
      # Eliminar aristas que formen ciclos
      for i in range(len(vertices)):
         lista = []
         for v in vertices[i]:
            cliclo = False
            for arista in aristas[i]:
               if arista.getDestino() == v.getNombre():
                  cliclo = True
                  break
            if not cliclo:
               lista.append(a)
         aristas[i] = lista
      aristasMin = []
      # Obtener arista menor de un conjunto
      for i in range(len(aristas)):
         menor = self.obtenerAristaMenor(aristas[i])
         aristasMin.append(aristas[i].pop(aristas[i].index(menor)))
      # Crear conjuntos
      conjuntos = []
      for arista in aristasMin:
         listaAux = [-1,-1]
         for num in range(len(vertices)):
            for vertice in vertices[num]:
               if arista.getOrigen() == vertice.getNombre():
                  listaAux[0] = num
               if arista.getDestino() == vertice.getNombre():
                  listaAux[1] = num
         conjuntos.append(listaAux)
      # Unir conjuntos



   def aristasAnchura(self, origen):
      self.recorridoAnchura(origen)
      vertices = []
      recorrido = []
      for v in self.anchura:
         vertices.append(self.obtenerVertice(v,self.listaVertices))
      for vertice in vertices:
         for adyacente in vertice.getListaAdyacentes():
            visitado = False
            for a in recorrido:
               if adyacente == a.getDestino() or adyacente == origen:
                  visitado = True
                  break
            if not visitado:
               recorrido.append(self.obtenerArista(vertice.getNombre(),adyacente, self.listaAristas))
      return recorrido


   def boruvka(self):
      copiaNodos = copy(self.listaVertices)  # copia de los nodos
      copiaAristas = copy(self.listaAristas)  # copia de las aristas

      AristasBorukvka = []
      ListaConjuntos = []
      bandera=True
      cantidad=0
      while(cantidad>1 or bandera):
         for Nodo in copiaNodos:
            bandera=False
            cantidad=self.Cantidadconjuntos(ListaConjuntos)

      rutas= self.OperacionesconjuntosB(Nodo, ListaConjuntos, AristasBorukvka,copiaAristas)
      return rutas

   def Cantidadconjuntos(self,ListaConjuntos):
      cantidad=0
      for conjunto in ListaConjuntos:
         if len(conjunto)>0:
            cantidad=cantidad+1
      return cantidad
   
   def OperacionesconjuntosB(self,Nodo, ListaConjuntos, AristasBorukvka,copiaAristas):
      encontrado1=-1
      encontrado2=-1
      # menor = self.Buscarmenor(Nodo, copiaAristas)

      if not None==None:#si no esta vacio
         if not ListaConjuntos:#si esta vacia
            ListaConjuntos.append({menor.getOrigen(),menor.getDestino()})
            AristasBorukvka.append(menor)
         else:
            for i in range(len(ListaConjuntos)):
               if  (menor.getOrigen()  in ListaConjuntos[i]) and (menor.getDestino() in ListaConjuntos[i]):
                  return False;##Camino cicliclo

            for i in range(len(ListaConjuntos)):
               if menor.getOrigen() in ListaConjuntos[i]:
                  encontrado1=i
               if menor.getDestino() in ListaConjuntos[i]:
                  encontrado2=i

            if encontrado1!=-1 and encontrado2!=-1:
               if encontrado1!=encontrado2:#si pertenecen a dos conjuntos diferentes
                  #debo unir los dos conjuntos
                  ListaConjuntos[encontrado1].update(ListaConjuntos[encontrado2])
                  ListaConjuntos[encontrado2].clear();#elimino el conjunto
                  AristasBorukvka.append(menor)

            if encontrado1!=-1 and encontrado2==-1:# si va unido por un conjunto
               ListaConjuntos[encontrado1].update(menor.getOrigen())
               ListaConjuntos[encontrado1].update(menor.getDestino())
               AristasBorukvka.append(menor)

            if encontrado1 == -1 and encontrado2 != -1:# si va unido por un conjunto
               ListaConjuntos[encontrado2].update(menor.getOrigen())
               ListaConjuntos[encontrado2].update(menor.getDestino())
               AristasBorukvka.append(menor)

            if encontrado1 == -1 and encontrado2 == -1:# si no existe en los conjuntos
               ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
               AristasBorukvka.append(menor)
      return self.kruskal()


   def Buscarmenor(self,Nodo,copiaAristas):
      temp=[]
      for adyacencia in Nodo.getListaAdyacentes():
         for Arista in copiaAristas:
            #busco las aristas de esa lista de adyacencia
            if Arista.getOrigen()==Nodo.getNombre() and Arista.getDestino()==adyacencia:
               temp.append(Arista)
      if temp:#si no esta vacia
         #una vez obtenga todas las aristas, saco la menor
         self.Ordenar(temp)  # ordeno las aristas
         #elimin ese destino porque ya lo voy a visitar
         #print("{0}-{1}:{2}".format(temp[0].getOrigen(), temp[0].getDestino(), temp[0].getPeso()))

         Nodo.getListaAdyacentes().remove(temp[0].getDestino())
         return temp[0]  # es la menor

      return None#es la menor
      


      




