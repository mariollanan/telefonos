import sqlite3 as sql
from unicodedata import name

def crear_db():
    conn = sql.connect("alumnos.db")
    conn.commit()
    conn.close()

def crear_Tabla():
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE alumnos(
            nombre text,
            edad integer
        )"""
    )
    conn.commit()
    conn.close()
def agregarReg(nombre,edad):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    agregar = f"INSERT INTO alumnos VALUES ('{nombre}', {edad})"
    cursor.execute(agregar)
    conn.commit()
    conn.close()

def agregarMuchosReg(muchosNombres):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    agregar = f"INSERT INTO alumnos VALUES (?, ?)"
    cursor.executemany(agregar,muchosNombres)
    conn.commit()
    conn.close()

def LeerReg():
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    consulta = f"SELECT * FROM alumnos"
    cursor.execute(consulta)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def ordenaTablaAlum(campo):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    # si pongo DESC lo ordena en forma descendente
    consulta = f"SELECT * FROM alumnos ORDER BY {campo}"
    cursor.execute(consulta)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def buscarReg(nombre):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    consulta = f"SELECT * FROM alumnos WHERE nombre='{nombre}'"
    cursor.execute(consulta)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
def BorrarReg(nombre):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    consulta = f"DELETE FROM alumnos WHERE nombre='{nombre}'"
    cursor.execute(consulta)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)



if __name__ == "__main__":
   crear_db()
