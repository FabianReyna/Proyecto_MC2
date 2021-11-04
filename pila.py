class Elemento:
    def __init__(self,elemento):
        self.elemento=elemento
        self.ant=None

class pila:
    def __init__(self):
        self.inicio=None
        self.fin=None

    def apilar(self,elemento):
        el=Elemento(elemento)
        
        if self.inicio==None:
            self.inicio=el
            self.inicio.ant=None
            self.fin=el

        else:
            self.inicio.ant=el
            self.inicio=self.inicio.ant