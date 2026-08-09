import funciones

def insertar(codigo,nombre,descripcion,categoria,precioBruto,precioNeto,stock,t_precio,conexionBD):
    try:
        if conexionBD!=None:
          cursor=conexionBD.cursor()
          cursor.execute("insert into productos values (%s,%s,%s,%s,%s,%s,%s,%s)",(codigo,nombre,descripcion,categoria,precioBruto,precioNeto,stock,t_precio))

          conexionBD.commit()
          return True
        else:
          return False   
    except:
        return False 
    
def consultar(conexionBD):
    try:
       if conexionBD!=None:
           cursor=conexionBD.cursor()
           cursor.execute("select * from productos")
           return cursor.fetchall()
       else:
           return []
    except:
        return []  

def vaciar(conexionBD):
    try:
        if conexionBD!=None:
          cursor=conexionBD.cursor()
          cursor.execute("delete from productos") 
          cursor.execute("alter table productos auto_increment=0") 
          conexionBD.commit()
          return True
        else:
          return False   
    except:
        return False         

def buscarNombre(nombre, conexionBD):
        try:
            if conexionBD!=None:
                cursor=conexionBD.cursor()
                cursor.execute("select * from productos where nombre = %s", (nombre,))
                return cursor.fetchall()
            else:
                return []
        except:
            return []

def buscarCodigo(codigo, conexionBD):
        try:
            if conexionBD!=None:
                cursor=conexionBD.cursor()
                cursor.execute("select * from productos where codigo = %s", (codigo,))
                return cursor.fetchall()
            else:
                return []
        except:
            return []


    
def eliminarNombre(nombre, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from productos where nombre = %s", (nombre,))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False

def eliminarCodigo(codigo, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from productos where codigo = %s", (codigo,))
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False



def modificarCodigo(n_codigo,nombre,descripcion,categoria,precio_bruto,precio_neto,stock,precio_total,codigo,conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("update productos set codigo= %s, nombre = %s, descripcion = %s, categoria = %s,precio_bruto= %s, precio_neto= %s, stock = %s, precio_total = %s   where codigo = %s",
            (n_codigo,nombre,descripcion,categoria,precio_bruto,precio_neto,stock,precio_total,codigo))          
            conexionBD.commit()
            return True
        else:
            return False
    except:
        return False
