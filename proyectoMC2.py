from tkinter import *
from tkinter.ttk import *
from analizadorLexico import *
from tkinter import simpledialog
from analizadorSintactico import analizadorSintactico
from pila import pila
import re
from tkinter import messagebox

scanner = AnalizadorLexico()
root=Tk()
frame = Frame(root)

numerador1=Text(root,wrap=NONE)
denominador1=Text(root,wrap=NONE)

operador1=Text(root,wrap=NONE)

numerador2=Text(root,wrap=NONE)
denominador2=Text(root,wrap=NONE)

operador2=Text(root,wrap=NONE)

numerador3=Text(root,wrap=NONE)
denominador3=Text(root,wrap=NONE)
lb_not_pol=Label(root,text='',background='skyblue')
lb_res=Label(root,text='',background='skyblue')



def main():
    root.title('Proyecto MC2N')
    root.resizable(False, False)
    root.geometry('950x300')
    root.config(bg='skyblue')
    numerador1.place(x=50,y=50,height=30,width=250)
    Label(root,text='--------------------------------------------------',background='skyblue').place(x=50,y=85)
    denominador1.place(x=50,y=110,height=30,width=250)

    operador1.place(x=310,y=80,height=30,width=30)




    numerador2.place(x=350,y=50,height=30,width=250)
    Label(root,text='--------------------------------------------------',background='skyblue').place(x=350,y=85)
    denominador2.place(x=350,y=110,height=30,width=250)

    operador2.place(x=610,y=80,height=30,width=30)

    numerador3.place(x=650,y=50,height=30,width=250)
    Label(root,text='--------------------------------------------------',background='skyblue').place(x=650,y=85)
    denominador3.place(x=650,y=110,height=30,width=250)
    Button(root,text='Operar',command=operar).place(x=410,y=175,width=100,height=30)
    lb_not_pol.place(x=350,y=225)
    lb_res.place(x=350,y=260)
    root.mainloop()


def operar():
    cadena1='('+numerador1.get('1.0', 'end').strip()+')/('+denominador1.get('1.0', 'end').strip()+')'
    cadena2='('+numerador2.get('1.0', 'end').strip()+')/('+denominador2.get('1.0', 'end').strip()+')'
    cadena3='('+numerador3.get('1.0', 'end').strip()+')/('+denominador3.get('1.0', 'end').strip()+')'
    cadenaTotal='('+cadena1+')'+operador1.get('1.0','end').strip()+'('+cadena2+')'+operador2.get('1.0','end').strip()+'('+cadena3+')'
    cadenaTotal=cadenaTotal.strip()
    
    scanner.analizar(cadenaTotal)
    diccionario=dict()
    copiaLista=list()
    lista_vars=list()
    for a in scanner.listaT:
        copiaLista.append(a)
        
        if a.tipo=='VARIABLE' and a.lexema not in lista_vars:
            lista_vars.append(a.lexema)
            diccionario[a.lexema]=simpledialog.askstring('Ingreso de valores','valor de '+a.lexema)
        else:
            pass

    
    
    copiaLista.reverse()
    pila_prefija=pila()
    stack=list()
    for a in copiaLista:
        if a.tipo=='VARIABLE':
            pila_prefija.apilar('['+a.lexema+']')
        
        elif a.tipo=='NUMERO':
            pila_prefija.apilar('['+a.lexema+']')
        
        elif a.tipo=='PARENTESIS2':
            stack.append(a.lexema)
        
        elif a.tipo=='PARENTESIS1':
            try:
                tmp=stack.pop()
                while tmp!=')':
                    pila_prefija.apilar(tmp)
                    tmp=stack.pop()
            except:
                pass
            
        elif a.tipo=='SUMA' or a.tipo=='RESTA':
            if len(stack)==0:
                stack.append(a.lexema)

            else:
                try:
                    if stack[-1]=='+' or stack[-1]=='-' or stack[-1]==')':
                        stack.append(a.lexema)
                    else:
                        tmp=stack.pop()
                        while tmp!='+' or tmp!='-':
                            pila_prefija.apilar(tmp)
                            if stack[-1]!=')':
                                tmp=stack.pop()
                                continue
                            break
                            
                        stack.append(a.lexema)
                except:
                    pass

        else:
            stack.append(a.lexema)
    
    if len(stack)!=0:
        try:
            while len(stack)!=0:
                pila_prefija.apilar(stack.pop())
        except:
            pass

    aux=pila_prefija.fin
    cadenaPrueba=''
    while aux!=None:
        cadenaPrueba=aux.elemento+cadenaPrueba
        aux=aux.ant
    cadenaPrueba=cadenaPrueba.replace('^','↑')
    lb_not_pol.config(text='NOTACION POLACA ' +cadenaPrueba)

    print(cadenaPrueba)

    for key in diccionario:
        cadenaPrueba=cadenaPrueba.replace(key,diccionario[key])
    
    div=re.search('\/(\[(\d+(\.\d)?)|([A-Z]))\]\[((\d+(\.\d)?)|([A-Z]))\]',cadenaPrueba)
    pro=re.search('\*(\[(\d+(\.\d)?)|([A-Z]))\]\[((\d+(\.\d)?)|([A-Z]))\]',cadenaPrueba)
    pot=re.search('\↑(\[(\d+(\.\d)?)|([A-Z]))\]\[((\d+(\.\d)?)|([A-Z]))\]',cadenaPrueba)
    sum=re.search('\+(\[(\d+(\.\d)?)|([A-Z]))\]\[((\d+(\.\d)?)|([A-Z]))\]',cadenaPrueba)
    res=re.search('\-(\[(\d+(\.\d)?)|([A-Z]))\]\[((\d+(\.\d)?)|([A-Z]))\]',cadenaPrueba)

    while div!= None or pro!=None or pot!=None or sum!=None or res!=None:

        if div!=None:
            separa=re.split('\[',div[0])
            separa[1]=separa[1].replace(']','')
            separa[2]=separa[2].replace(']','')
            

            separa[1]=float(separa[1])
            
            separa[2]=float(separa[2])

            operar=separa[1]/separa[2]
            cadenaPrueba=cadenaPrueba.replace(div[0],'['+str(operar)+']')
        
        if pro!=None:
            separa=re.split('\[',pro[0])
            separa[1]=separa[1].replace(']','')
            separa[2]=separa[2].replace(']','')
            

            separa[1]=float(separa[1])
            
            separa[2]=float(separa[2])

            operar=separa[1]*separa[2]
            cadenaPrueba=cadenaPrueba.replace(pro[0],'['+str(operar)+']')

        if pot!=None:
            separa=re.split('\[',pot[0])
            separa[1]=separa[1].replace(']','')
            separa[2]=separa[2].replace(']','')
            

            separa[1]=float(separa[1])
            
            separa[2]=float(separa[2])

            operar=separa[1]**separa[2]
            cadenaPrueba=cadenaPrueba.replace(pot[0],'['+str(operar)+']')
    
        if sum!=None:
            separa=re.split('\[',sum[0])
            separa[1]=separa[1].replace(']','')
            separa[2]=separa[2].replace(']','')
        
            separa[1]=float(separa[1])
            separa[2]=float(separa[2])

            operar=separa[1]+separa[2]
            cadenaPrueba=cadenaPrueba.replace(sum[0],'['+str(operar)+']')

        if res!=None:
            separa=re.split('\[',res[0])
            separa[1]=separa[1].replace(']','')
            separa[2]=separa[2].replace(']','')
            

            separa[1]=float(separa[1])
            separa[2]=float(separa[2])

            operar=separa[1]-separa[2]
            cadenaPrueba=cadenaPrueba.replace(res[0],'['+str(operar)+']')

        div=re.search('\/(\[\d+(\.\d)?|[A-Z])\]\[(\d+(\.\d)?|[A-Z])\]',cadenaPrueba)
        pro=re.search('\*(\[\d+(\.\d)?|[A-Z])\]\[(\d+(\.\d)?|[A-Z])\]',cadenaPrueba)
        pot=re.search('\↑(\[\d+(\.\d)?|[A-Z])\]\[(\d+(\.\d)?|[A-Z])\]',cadenaPrueba)
        sum=re.search('\+(\[\d+(\.\d)?|[A-Z])\]\[(\d+(\.\d)?|[A-Z])\]',cadenaPrueba)
        res=re.search('\-(\[\d+(\.\d)?|[A-Z])\]\[(\d+(\.\d)?|[A-Z])\]',cadenaPrueba)
    

    lb_res.config(text='RESPUESTA '+cadenaPrueba)
        

    




    # for a in copiaLista:
    #     if a.tipo=='NUMERO':
    #         lista_aux.apilar('['+a.lexema+']')
    #     elif a.tipo=='VARIABLE':
    #         lista_aux.apilar(a.lexema)
    #     elif a.tipo=='POTENCIA' or a.tipo=='SUMA' or a.tipo=='RESTA' or a.tipo=='PRODUCTO' or a.tipo=='DIVISION':
    #         lista_aux2.apilar(a.lexema)
    #     elif a.tipo=='PARENTESIS1':

    #         la1=lista_aux.fin
    #         while la1!=None:
    #             lista_pila.apilar(la1.elemento)
    #             la1=la1.ant
    #         lista_aux=pila()

    #         la2=lista_aux2.fin
    #         while la2!=None:
    #             lista_pila.apilar(la2.elemento)
    #             la2=la2.ant
    #         lista_aux2=pila()

    # asd=lista_pila.fin
    # cadena_ver=''
    # while asd!=None:
    #     cadena_ver=asd.elemento+cadena_ver
    #     asd=asd.ant
    #print(cadena_ver)
        


if __name__ == "__main__":
    main()