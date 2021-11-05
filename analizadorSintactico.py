from pila import *


class analizadorSintactico:
    def __init__(self,tokens:list):
        self.tokens=tokens
        self.tokens.reverse()
        self.listaOficial=pila()
        self.listaAux1=pila()
        self.listaAux2=pila()

    def analizar(self):
        self.INICIO()

    def INICIO(self):
        self.INSTRUCCIONES()

    def INSTRUCCIONES(self):
        self.EXPRESION()




    def EXPRESION(self):
        try:
            tmp=self.tokens.pop()
            if tmp.tipo=='PARENTESIS1':
                self.EXPRESION()
                tmp=self.tokens.pop()
                if tmp.tipo=='PARENTESIS2':
                    aux=self.listaAux1.fin
                    while aux!=None:
                        self.listaOficial.apilar(aux.elemento)
                        aux=aux.ant
                    self.listaAux1=pila()

                    aux=self.listaAux2.fin
                    while aux!=None:
                        self.listaOficial.apilar(aux.elemento)
                        aux=aux.ant
                    self.listaAux2=pila()
                    self.EXPRESION()
            
            elif tmp.tipo=='NUMERO':
                self.listaAux1.apilar('['+tmp.lexema+']')
                self.EXPRESION()

            elif tmp.tipo=='VARIABLE':
                self.listaAux1.apilar(tmp.lexema)
                self.EXPRESION()

            elif tmp.tipo=='SUMA':
                self.listaAux2.apilar(tmp.lexema)
                self.EXPRESION()
            
            elif tmp.tipo=='POTENCIA':
                self.listaAux2.apilar(tmp.lexema)
                self.EXPRESION()

            elif tmp.tipo=='RESTA':
                self.listaAux2.apilar(tmp.lexema)
                self.EXPRESION()
            
            elif tmp.tipo=='PRODUCTO':
                self.listaAux2.apilar(tmp.lexema)
                self.EXPRESION()

            
            elif tmp.tipo=='DIVISION':
                self.listaAux2.apilar(tmp.lexema)
                self.EXPRESION()

            elif tmp.tipo=='PARENTESIS2':
                    aux=self.listaAux1.fin
                    while aux!=None:
                        self.listaOficial.apilar(aux.elemento)
                        aux=aux.ant
                    self.listaAux1=pila()

                    aux=self.listaAux2.fin
                    while aux!=None:
                        self.listaOficial.apilar(aux.elemento)
                        aux=aux.ant
                    self.listaAux2=pila()
                    self.EXPRESION()
        except:
            pass

                
                
