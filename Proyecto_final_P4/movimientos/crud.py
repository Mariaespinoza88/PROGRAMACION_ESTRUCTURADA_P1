'''
Crud de la tabla de movimientos, nos permite ingresar el tipo de movimiento, cantidad y fecha del movimiento

'''
def insertar(codigo, nombre, cantidad, tipo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("INSERT INTO movimientos (codigo, nombre, cantidad, tipo) VALUES (%s,%s,%s,%s)",
                           (codigo, nombre, cantidad, tipo))
            
            if tipo == "ENTRADA" or tipo == "E":
                cursor.execute("UPDATE productos SET stock = stock + %s WHERE codigo = %s", (cantidad, codigo))
            elif tipo == "SALIDA" or tipo == "S":
                cursor.execute("UPDATE productos SET stock = stock - %s WHERE codigo = %s", (cantidad, codigo))   
            
            cursor.execute("UPDATE productos SET precio_total = precio_neto * stock WHERE codigo = %s", (codigo,))
            
            conexionBD.commit()
            return True
        return False
    except:
        return False

def consultar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM movimientos")
            return cursor.fetchall()
        return []
    except:
        return []

def buscar(id_movimiento, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM movimientos WHERE id = %s", (id_movimiento,))
            return cursor.fetchall()
        return []
    except:
        return []

def buscarNombre(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM productos WHERE nombre = %s", (nombre,))
            return cursor.fetchall()
        return []
    except:
        return []

def eliminar(id_movimiento, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM movimientos WHERE id = %s", (id_movimiento,))
            conexionBD.commit()
            return True
        return False
    except:
        return False

def vaciar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM movimientos")
            cursor.execute("ALTER TABLE movimientos AUTO_INCREMENT=0")
            conexionBD.commit()
            return True
        return False
    except:
        return False

def modificar(id_movimiento, cantidad, tipo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("UPDATE movimientos SET cantidad = %s, tipo = %s WHERE id = %s",
                           (cantidad, tipo, id_movimiento))
            conexionBD.commit()
            return True
        return False
    except:
        return False

