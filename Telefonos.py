###########################################################
#
#  Sistema Telefonos
# Autor: Mario Llanan
# email: mario.llanan@gmail.com
#
##########################################################
# Esta es una line a de prueba de git
#importo modulo de conexion con la db
import TelConexion
#importo tkinter
from tkinter import*
from tkinter.ttk import*
from tkinter import Frame

ventana=Tk()
ventana.title("Telefonos")
ventana.geometry("800x600")
frame1 = Frame(ventana, bg="blue")
frame1.pack()
#expand=True, fill='both'
def captura():
    nombre = str(txtNombre.get())
    apellido = str(txtApellido.get())
    telefono = str(txtTelefono.get())

#Etiquetas
lblTitulo = Label(ventana, text="Sistema Telefonos V1.0")
lblsubAnuncio = Label(ventana, text="SSI Systems")
lblApellido = Label(ventana, text="Apellido :")
lblNombre = Label(ventana, text="Nombre :")
lbltelfono = Label(ventana, text="Telefono:")

#Entradas

txtNombre = Entry(ventana, font="Helvetica 12", width=60)
txtApellido = Entry(ventana, font="Helvetica 12", width=60)
txtTelefono = Entry(ventana, font="Helvetica 12", width=25)
#BOTONES

btnGuardar = Button(ventana, text="Guardar" , command= captura)

#places 

lblTitulo.pack()
lblsubAnuncio.pack()
lblApellido.place(x= 20, y=20)
lblNombre.place(x=20,y=45)
lbltelfono.place(x=20, y=70)
txtNombre.place(x=80, y=20)
txtApellido.place(x=80, y=45)
txtTelefono.place(x=80, y=70)
btnGuardar.place(x=20,y=110) 

ventana.mainloop()