class Control:

    ##constructor con atributo tv de tipo TV, reservándole espacio en memoria
    def __init__ (self):
        self.tv=None

    ##metodo para encender el tv
    def turnOn (self):
        self.tv.estado=True

    ##metodo para apagar el tv
    def turnOff(self):
        self.tv.estado=False

    ##getters  y setters atributo tv
    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv=tv

    ##metodo subir canal
    def canalUp(self):
        if (self.tv.estado==True and self.tv.canal>=1 and self.tv.canal !=120):
            self.tv.canal+=1

    ##metodo bajar canal
    def canalDown(self):
        if (self.tv.estado==True and self.tv.canal>1 and self.tv.canal <= 120):
            self.tv.canal-=1

    ##metodo subir volumen
    def volumenUp(self):
        if (self.tv.estado==True and self.tv.volumen >=0 and self.tv.volumen !=7):
            self.tv.volumen+=1
            
    ##metodo ajustar canal
    def setCanal(self, canal):
        if (self.tv.estado==True):
            self.tv.canal=canal

    ##metodo bajar volumen
    def volumenDown(self):
        if (self.tv.estado==True and self.tv.volumen >0 and self.tv.volumen <=7):
            self.tv.volumen-=1

    ##metodo enlazar
    def enlazar(self,tv):
        self.tv=tv
        self.tv.control=self


