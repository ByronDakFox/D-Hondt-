
from tkinter import *

listaT = []
listaEscaños = []
def ValorMin():
    suma=(int(P1.get())+int(P2.get())+int(P3.get())+int(P4.get())+int(P5.get()))
    porcentaje=(int(liston.get())/100)
    valorMinimo=(int(suma)*porcentaje)
    valorMinimo=round(valorMinimo,0)
    valorMin.set(int(valorMinimo))
    votosTotal.set(suma)
    Escanios=int(escanios.get())
    p1=int(P1.get())

    for i in range(1,Escanios+1):
        a=int(P1.get())/i
        a=round(a,0)
        i+=1
        lista.append(a)
    print(lista)
    for i in range(1,Escanios+1):
        a=int(P2.get())/i
        a=round(a,0)
        i+=1
        lista2.append(a)
    print(lista2)
    for i in range(1,Escanios+1):
        a=int(P3.get())/i
        a=round(a,0)
        i+=1
        lista3.append(a)
    print(lista3)
    for i in range(1,Escanios+1):
        a=int(P4.get())/i
        a=round(a,0)
        i+=1
        lista4.append(a)
    print(lista4)
    for i in range(1,Escanios+1):
        a=int(P5.get())/i
        a=round(a,0)
        i+=1
        lista5.append(a)
    print(lista5)
    for i in range(Escanios):
        listaT.append(lista[i])
        listaT.append(lista2[i])
        listaT.append(lista3[i])
        listaT.append(lista4[i])
        listaT.append(lista5[i])
    listaT.sort(reverse=True)
    for i in range(Escanios):
        listaEscaños.append(listaT[i])
    print("Lista de Escaños: ", listaEscaños)

    cont = 0
    for i in range(Escanios):
        numT = lista[i]
        for j in range(len(listaEscaños)):
            if numT == listaEscaños[j]:
                num = j
                cont = cont + 1
                boole = True
                break

        if boole == True:
            listaEscaños.pop(num)
            boole = False

    print("Lista A: ", cont," Escaños")

    cont = 0
    for i in range(Escanios):
        numT = lista2[i]
        for j in range(len(listaEscaños)):
            if numT == listaEscaños[j]:
                num = j
                cont = cont + 1
                boole = True
                break

        if boole == True:
            listaEscaños.pop(num)
            boole = False

    print("Lista B: ", cont," Escaños")

    cont = 0
    for i in range(Escanios):
        numT = lista3[i]
        for j in range(len(listaEscaños)):
            if numT == listaEscaños[j]:
                num = j
                cont = cont + 1
                boole = True
                break

        if boole == True:
            listaEscaños.pop(num)
            boole = False

    print("Lista C: ", cont," Escaños")

    cont = 0
    for i in range(Escanios):
        numT = lista4[i]
        for j in range(len(listaEscaños)):
            if numT == listaEscaños[j]:
                num = j
                cont = cont + 1
                boole = True
                break

        if boole == True:
            listaEscaños.pop(num)
            boole = False

    print("Lista D: ", cont," Escaños")

    cont = 0
    for i in range(Escanios):
        numT = lista5[i]
        for j in range(len(listaEscaños)):
            if numT == listaEscaños[j]:
                num = j
                cont = cont + 1
                boole = True
                break

        if boole == True:
            listaEscaños.pop(num)
            boole = False

    print("Lista E: ", cont," Escaños")





#ventana principal
ventana=Tk()
ventana.title("Cuamacas - Ramirez - Toapanta - Sistema D'Hondt")
#anchoxalto
ventana.geometry("380x460")
lista=[]
lista2=[] 
lista3=[] 
lista4=[] 
lista5=[]         

#variables
valorMin= StringVar()
votosTotal= StringVar()

escanios=StringVar()
escanios.set("0")
liston=StringVar()
liston.set("0")
blanco=StringVar()
blanco.set("0")
P1=StringVar()
P1.set("0")
P2=StringVar()
P2.set("0")
P3=StringVar()
P3.set("0")
P4=StringVar()
P4.set("0")
P5=StringVar()
P5.set("0")
Partido1=StringVar()
Partido1.set("Lista A")
Partido2=StringVar()
Partido2.set("Lista B")
Partido3=StringVar()
Partido3.set("Lista C")
Partido4=StringVar()
Partido4.set("Lista D")
Partido5=StringVar()
Partido5.set("Lista E")
#labels
lblEscanios=Label(text="Número de Escaños a repartir: ",font=("Arial",10)).place(x=10,y=20)

lblliston=Label(text="Listón Electoral(%): ",font=("Arial",10)).place(x=10,y=40)
lblBlancos=Label(text="Votos en Blanco: ",font=("Arial",10)).place(x=10,y=60)
lblP1=Entry(ventana,justify="center",textvariable=Partido1,font=("Arial",10)).place(x=10,y=100)
lblP2=Entry(ventana,justify="center",textvariable=Partido2,font=("Arial",10)).place(x=10,y=120)
lblP3=Entry(ventana,justify="center",textvariable=Partido3,font=("Arial",10)).place(x=10,y=140)
lblP4=Entry(ventana,justify="center",textvariable=Partido4,font=("Arial",10)).place(x=10,y=160)
lblP5=Entry(ventana,justify="center",textvariable=Partido5,font=("Arial",10)).place(x=10,y=180)
lblMin=Label(text="Mínimo votos para acceder a un escaño: ",font=("Arial",8)).place(x=0,y=200)
lblVTotal=Label(text="Número de votos total: ",font=("Arial",8)).place(x=0,y=225)
#textbox
txtEscanios=Entry(ventana,justify="center",textvariable=escanios).place(x=200,y=20)
txtListon=Entry(ventana,justify="center",textvariable=liston).place(x=200,y=40)
txtBlancos=Entry(ventana,justify="center",textvariable=blanco).place(x=200,y=60)
txtP1=Entry(ventana,justify="center",textvariable=P1).place(x=175,y=100)
txtP2=Entry(ventana,justify="center",textvariable=P2).place(x=175,y=120)
txtP3=Entry(ventana,justify="center",textvariable=P3).place(x=175,y=140)
txtP4=Entry(ventana,justify="center",textvariable=P4).place(x=175,y=160)
txtP5=Entry(ventana,justify="center",textvariable=P5).place(x=175,y=180)

txtValorMin=Entry(ventana, justify="center", textvariable=valorMin, state="disabled").place(x=220,y=205)
txtVTotal=Entry(ventana, justify="center", textvariable=votosTotal, state="disabled").place(x=220,y=225)





Button(ventana, text="Calcular", command=ValorMin).place(x=120,y=250)
ventana.mainloop()

