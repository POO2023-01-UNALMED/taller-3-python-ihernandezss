class TV:
    numTV=0

    def __init__ (self, marca, estado):
        self.marca=marca
        self.estado=estado
        self.control=None
        self.canal=1
        self.volumen=1
        self.precio=500
        TV.numTV+=1
    
    #setters y getters
    def setMarca (self,marca):
        self.marca=marca

    def setControl (self,control):
        self.control=control

    def setPrecio (self,precio):
        self.precio=precio

    def setVolumen (self,volumen):
        if (self.estado==True):
            self.volumen=volumen

    def setCanal (self,canal):
        if (self.estado==True and canal>=1 and canal<=120):
            self.canal=canal

    def getMarca (self):
        return self.marca
    
    def getControl(self):
        return self.control
    
    def getPrecio(self):
        return self.precio
    
    def getVolumen(self):
        return self.volumen
    
    def getCanal(self):
        return self.canal
    
    def getEstado(self):
        return self.estado
        

    ##setter y getter del atributo de clase numTV, el cual necesariamente tiene un método de clase
    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    ##metodo para encender televisor
    def turnOn(self):
        self.estado=True

    ##metodo para apagar televisor
    def turnOff(self):
        self.estado=False

    ##metodo para subir canal
    def canalUp(self):
        if (self.estado==True and self.canal>=1 and self.canal != 120):
            self.canal+=1

    ##metodo para bajar canal
    def canalDown(self):
        if (self.estado==True and self.canal>1 and self.canal <=120 ):
            self.canal-=1

    ##metodo para subir volumen
    def volumenUp(self):
        if (self.estado==True and self.volumen>=0 and self.volumen!=7):
            self.volumen+=1
            
    ##metodo para bajar volumen
    def volumenDown(self):
        if (self.estado==True and self.volumen>0 and self.volumen<=7):
            self.volumen-=1
