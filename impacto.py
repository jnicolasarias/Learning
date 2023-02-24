import math

#Constantes
DMS = 1.5 * (10**11)

#Fin Constantes


#Clase Tierra--------------------------------------------------------
class Tierra:

    def __init__(self, masa, velocidadx, velocidady, posicionx, posiciony):
        self.masa = masa
        self.velocidadx = velocidadx
        self.velocidady = velocidady
        self.posicionx = posicionx
        self.posiciony = posiciony

    #Metodos Funcionales
    def actualizar_posicionx(self, posicionx):
        self.posicionx = posicionx

    def actualizar_posiciony(self, posiciony):
        self.posiciony = posiciony

    def actualizar_velocidad(self, velocidad):
        self.velocidad = velocidad

    #Metodos Comunicativos
    def dar_posicionx(self):
        return self.posicionx

    def dar_posiciony(self):
        return self.posiciony

    def dar_velocidad(self):
        return self.velocidad


#--------------------------------------------------------------------


#Clase Asteroide-----------------------------------------------------
class Asteroide:

    def __init__(self, masa, velocidadx, velocidady, posicionx, posiciony):
        self.masa = masa
        self.velocidadx = velocidadx
        self.velocidady = velocidady
        self.posicionx = posicionx
        self.posiciony = posiciony

    #Metodos Funcionales
    def actualizar_posicionx(self, posicionx):
        self.posicionx = posicionx

    def actualizar_posiciony(self, posiciony):
        self.posiciony = posiciony

    def actualizar_velocidad(self, velocidad):
        self.velocidad = velocidad

    #Metodos Comunicativos
    def dar_posicionx(self):
        return self.posicionx

    def dar_posiciony(self):
        return self.posiciony

    def dar_velocidad(self):
        return self.velocidad


#--------------------------------------------------------------------

tierra = Tierra(6 * (10**24), 0, 30000, DMS, 0)
asteroide = Asteroide(15 * (10**14), 25000 / 2, 25000.0 * (math.sqrt(3.0)) / 2,
                      (999.0 / 1000) * DMS, 0)
