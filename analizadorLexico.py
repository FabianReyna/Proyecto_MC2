from Token import Token

class AnalizadorLexico:
    def __init__(self):
        self.listaT=list()
        self.buffer=''
        self.estado=0
        self.i=0
    
    def NewToken(self,lex,tip):
        self.listaT.append(Token(lex,tip))
    
    def estado0(self,caracter:str):
        if caracter == ')':
            self.NewToken(caracter, 'PARENTESIS2')
            self.buffer = ''
            
        elif caracter == '(':
            self.NewToken(caracter, 'PARENTESIS1')
            self.buffer = ''
        
        elif caracter == '=':
            self.NewToken(caracter, 'IGUAL')
            self.buffer = ''
        
        elif caracter == '^':
            self.NewToken(caracter, 'POTENCIA')
            self.buffer = ''
        
        elif caracter == '+':
            self.NewToken(caracter, 'SUMA')
            self.buffer = ''
        
        elif caracter == '-':
            self.NewToken(caracter, 'RESTA')
            self.buffer = ''
        
        elif caracter == '*':
            self.NewToken(caracter, 'PRODUCTO')
            self.buffer = ''
        
        elif caracter == '/':
            self.NewToken(caracter, 'DIVISION')
            self.buffer = ''
        
        elif caracter.isdigit():
            self.buffer = caracter
            self.estado = 1
        
        elif caracter.isalpha():
            self.NewToken(caracter, 'VARIABLE')
            self.buffer = ''
    
    def estado1(self,caracter:str):
        if caracter.isdigit():
            self.buffer += caracter
            
        elif caracter == '.':
            self.buffer += caracter
            self.estado = 2

        else:
            self.NewToken(self.buffer, 'NUMERO')
            self.i -= 1
            self.buffer = ''
            self.estado = 0
    
    def estado2(self, caracter:str):
        if caracter.isdigit():
            self.buffer += caracter
        else:
            self.NewToken(self.buffer, 'NUMERO')
            self.buffer = ''
            self.i -= 1
            self.estado = 0
    
    def analizar(self, cadena):
            self.listaT = list()
            self.buffer = ''
            self.estado = 0
            self.i = 0

            while self.i < len(cadena):
                if self.estado == 0:
                    self.estado0(cadena[self.i])

                elif self.estado == 1:
                    self.estado1(cadena[self.i])

                elif self.estado == 2:
                    self.estado2(cadena[self.i])
                
                self.i+=1