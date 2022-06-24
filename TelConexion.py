#importo la libreria sqlite3
import sqlite3 as sql

from matplotlib.pyplot import close
#creamos la base de datos 
def crearDbTel():
    conn = sql.connect("telefonos.db")
    conn.commit()
    conn.close()

#Creamos la Tabla dentro de la base de datos 

def crearTabla():
    conn = sql.connect("telefonos.db")
    cursor = sql.Cursor()
    cursor.execute("CREATE TABLE TELEFONOS (nombre VARCHAR(50), apellido VARCHAR(50), telefono VARCHAR (15))")
    conn.commit()
    conn.close()

