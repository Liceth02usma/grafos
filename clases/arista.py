"""— Clase arista —"""

class Arista:

    # Constructor
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""
    # Set - Get | origen
    def getOrigen(self):
        return self.origen

    def setOrigen(self, origen):
        self.origen = origen

    # Set - Get | destino
    def getDestino(self):
        return self.destino

    def setDestino(self, destino):
        self.destino = destino

    # Set - Get | peso
    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso


