#################################################
# Funcion cuadratica 
# Grupo 3 MEI 
# Informatica:Llanan Mario
# Matematicas:Ordenes Nicolas, Riquelme Ruth 
#################################################
# F(X)= 1000+360t-20t²
# f(x)=c+b*t-at²
#################################################

from tkinter import*
from tkinter.ttk import*
import math
from matplotlib.pyplot import text


ventana=Tk()
ventana.title("Grupo 3 Coformacion MEI")
ventana.geometry("400x600")
# proceso
def datear() :
    #Tomo los datos
    a = float(termino1.get())
    b = float(termino2.get())
    c = float(termino3.get())
    #calculo la poblacion inicial
    poblacionInicial = c+b*0-a*0
    #Preparo las etiquetas
    etMuestra["text"] = a
    etMuestra1["text"] = b
    etMuestra2["text"] = c
    etMuestraPI["text"] = poblacionInicial
    #muestro los resultados
    etMuestraPI0.place(x=20, y=180)
    etMuestraPI.place(x=120,y=180)
    #calculo las raices
    Raiz1= (-b + math.sqrt((b**2)-4*a*c))/(2*a)
    Raiz2= (-b - math.sqrt((b**2)-4*a*c))/(2*a)
    # etiquetas de Raices
    # #Raiz 1
    etMuestraLblR1 = Label(ventana,text="Raiz 1")
    etMuestraLblR1.place(x=20, y= 200)
    etMuestraRAiz1 = Label(ventana)
    etMuestraRAiz1["text"] = Raiz1
    etMuestraRAiz1.place(x=120, y= 200)
    #Raiz 2
    etMuestraLblR2 = Label(ventana,text="Raiz 2")
    etMuestraLblR2.place(x=20, y= 220)
    etMuestraRAiz2 = Label(ventana)
    etMuestraRAiz2["text"] = Raiz2
    etMuestraRAiz2.place(x=120, y= 220)
    #Vertice
    vertice= -(b)/(2*a)
    LblVertice = Label(ventana,text="Vertice")
    LblVertice.place(x=20, y= 240)
    LblVertice1 = Label(ventana)
    LblVertice1["text"] = vertice
    LblVertice1.place(x=120, y= 240)
    #Poblacion Maxima
    PobMaxima = c+(b*vertice)-((-a)*(vertice**2))
    LblPobMax = Label(ventana,text="Poblacion Max")
    LblPobMax.place(x=20, y= 260)
    LblPobMax1 = Label(ventana)
    LblPobMax1["text"] = PobMaxima
    LblPobMax1.place(x=120, y= 260)
    LblDiax.place(x=20, y=280)
    TxtDiaX = Entry(ventana, font="Helvetica 12", width=5)
    TxtDiaX.place(x=60, y=280)
    def diax():
        diacal = float(TxtDiaX.get())
        diaX = c+(b*diacal)-((-a)*(diacal**2))
        LblResDiax = Label(ventana)
        LblResDiax["text"] = diaX
        LblResDiax.place(x=120, y=280)

    boton2= Button(ventana, text = "DiaX",command=diax)
    boton2.place(x=20, y=320)
# etMuestra
etMuestra = Label(ventana)
etMuestra1 = Label(ventana)
etMuestra2 = Label(ventana)
etMuestraPI0 = Label(ventana, text="Poblacion Inicial")
etMuestraPI = Label(ventana)
# etiquetas
Titulo = Label(ventana, text="Calculo de Funcion Cuadratica")
EtTerm1 = Label(ventana, text="Primer Termino")
EtTerm2 = Label(ventana, text="Segundo Termino")
EtTerm3 = Label(ventana, text="Tercer Termino")
LblDiax = Label(ventana, text="DiaX")
# ingreso de datos
termino1 = Entry(ventana, font="Helvetica 12", width=5)
termino2 = Entry(ventana, font="Helvetica 12", width=5)
termino3 = Entry(ventana, font="Helvetica 12", width=5)
#botones
boton1= Button(ventana, text = "Calcular", command=datear)
boton3= Button(ventana, text = "Boton3")
# places
Titulo.pack()
EtTerm1.place(x=20,y=20)
termino1.place(x=120,y=20)
EtTerm2.place(x=20,y=50)
termino2.place(x=120,y=50)
EtTerm3.place(x=20,y=80)
termino3.place(x=120,y=80)
boton1.place(x=20,y=120)
etMuestra.place(x=20,y=160)
etMuestra1.place(x=60,y=160)
etMuestra2.place(x=100,y=160)
ventana.mainloop()