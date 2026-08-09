import funciones
from productos import crud

def agregarProducto(conexionBD):
    print("\n\t\t\t...::: AGREGAR PRODUCTO :::... \n")
    opc = "si"
    stock=0
    while opc == "si":
        codigo = int(funciones.validacion("Código del producto: ", r"^\d{1,10}$", "Ingrese un código correcto (1-10 dígitos)"))
        nombre = funciones.validacion("Nombre del producto: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese un nombre válido (A-Z, máx 20 caracteres)").upper().strip()
        descripcion = funciones.validacion("Descripción: ", r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]{1,25}$", "Ingrese una descripción válida (máx 25 caracteres)").upper().strip()
        categoria = funciones.validacion("Categoría: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese una categoría válida").upper().strip()
        precioBruto = round(float(funciones.validacion("Precio bruto: ", r"^\d+(\.\d{1,5})?$", "Ingrese un valor numérico correcto")), 2)
    
        
        precioNeto = funciones.neto(precioBruto)
        t_precio = round((precioNeto * stock), 2)
        
        respuesta = crud.insertar(codigo, nombre, descripcion, categoria, precioBruto, precioNeto, stock, t_precio, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
        
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas agregar otro producto? (si/no) ").lower().strip()
    funciones.esperarTecla()

def mostrarProductos(conexionBD):
    print("\n\t\t\t\t...:::: MOSTRAR PRODUCTOS ::::...\n")
    inventario = crud.consultar(conexionBD)

    total_articulos_stock = 0
    acumulador_valor_total = 0.0
    registros = 0

    if len(inventario) > 0:
        print(f"\t{'Codigo':<10}\t{'Nombre':<10}\t{'Descripción':<20}\t{'Categoria':<10}\t{'P. Bruto':<12}\t{'P. Neto':<12}\t{'Stock':<10}\t{'Total Precio':<12}\n")
        print("-" * 140)
        for i in inventario:
            print(f"\t{i[0]:<10}\t{i[1]:<10}\t{i[2]:<20}\t{i[3]:<10}\t{i[4]:<12}\t{i[5]:<12}\t{i[6]:<10}\t{i[7]:<12}")
            total_articulos_stock += i[6]
            acumulador_valor_total += float(i[7])
            registros += 1

        print("-" * 140)       
        promedio_precio = acumulador_valor_total / len(inventario) if len(inventario) > 0 else 0
        descuento_global = acumulador_valor_total * funciones.DESCUENTO_MAYOREO
        
        print(f"\n\t--> Total de artículos en stock: {total_articulos_stock}")
        print(f"\t--> Valor total del inventario: ${round(acumulador_valor_total, 2)}")
        print(f"\t--> Precio promedio por producto: ${round(promedio_precio, 2)}")
        print(f"\t--> Registros realizados: {registros}")
        print(f"\t--> Descuento aplicable por volumen (5%): ${round(descuento_global, 2)}")
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("\n¿Deseas generar un reporte en PDF? (Si/No) ").lower().strip()      
            if opc == "si":
                funciones.productosPDF(inventario)
    else:
        print("\n...¡No hay productos para mostrar!...")
    funciones.esperarTecla()

def limpiarProducto(conexionBD):
    print("\n\t\t\t...::: BORRAR TODOS LOS PRODUCTOS :::... \n")
    opc = ""
    while opc != "si" and opc != "no":
        opc = input("¿Estás seguro que deseas borrar TODOS los productos (si/no)? ").lower().strip()
    if opc == "si":
        if crud.vaciar(conexionBD):
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    funciones.esperarTecla()

def buscarProducto(conexionBD):
    print("\n\t\t\t...::: BUSCAR PRODUCTO :::... \n")
    opc = "si"
    while opc == "si":
        opcion = ""
        resultado = []
        while opcion != "nombre" and opcion != "codigo":
            opcion = input("\n¿Deseas buscar el producto por nombre o código? (Nombre/Código) ").lower().strip()        
            if opcion == "nombre":
                nombre = funciones.validacion("Nombre de producto: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese un nombre válido").upper().strip()
                resultado = crud.buscarNombre(nombre, conexionBD)
            elif opcion == "codigo":
                codigo = int(funciones.validacion("Código de producto: ", r"^\d{1,10}$", "Ingrese un código válido"))
                resultado = crud.buscarCodigo(codigo, conexionBD)
        if len(resultado) > 0:
            print(f"\t{'Codigo':<10}\t{'Nombre':<10}\t{'Descripción':<20}\t{'Categoria':<10}\t{'P. Bruto':<12}\t{'P. Neto':<12}\t{'Stock':<10}\n")
            print("-" * 130)
            for i in resultado:
                print(f"\t{i[0]:<10}\t{i[1]:<10}\t{i[2]:<20}\t{i[3]:<10}\t{i[4]:<12}\t{i[5]:<12}\t{i[6]:<10}")
            print("-" * 130)
            opc = ""
            while opc != "si" and opc != "no":
                opc = input("\n¿Deseas buscar otro producto? (si/no) ").lower().strip()
        else:
            print(f"\n\t... ¡Incorrecto, verifique! ...")
    funciones.esperarTecla()

def borrarProducto(conexionBD):
    print("\n\t\t\t...::: BORRAR PRODUCTO :::... \n")
    opcion = "si"
    while opcion == "si":
        opc = ""
        resultado = []
        while opc != "nombre" and opc != "codigo":
            opc = input("\n¿Deseas buscar el producto por nombre o código? (Nombre/Código) ").lower().strip()        
            if opc == "nombre":
                nombre = funciones.validacion("Nombre de producto: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese un nombre válido").upper().strip()
                resultado = crud.buscarNombre(nombre, conexionBD)
            elif opc == "codigo":
                codigo = int(funciones.validacion("Código de producto: ", r"^\d{1,10}$", "Ingrese un código válido"))
                resultado = crud.buscarCodigo(codigo, conexionBD)
        if len(resultado) > 0:
            print(f"\t{'Codigo':<10}\t{'Nombre':<10}\t{'Descripción':<20}\t{'Categoria':<10}\t{'Stock':<10}\n")
            print("-" * 100)
            for i in resultado:
                print(f"\t{i[0]:<10}\t{i[1]:<10}\t{i[2]:<20}\t{i[3]:<10}\t{i[6]:<10}")
            print("-" * 100)

            confirmacion = ""
            while confirmacion != "si" and confirmacion != "no":
                confirmacion = input("¿Estás seguro que deseas borrar el producto (si/no)? ").lower().strip()
                if confirmacion == "si":
                    if opc == "nombre":
                        if crud.eliminarNombre(nombre, conexionBD):
                            funciones.accionExitosa()
                        else:
                            funciones.accionNoExitosa()
               
                    elif opc == "codigo": 
                        if crud.eliminarCodigo(codigo, conexionBD):
                            funciones.accionExitosa()
                        else:
                            funciones.accionNoExitosa()


            opcion = ""
            while opcion != "si" and opcion != "no":
                opcion = input("\n¿Deseas borrar otro producto? (Si/No) ").lower().strip()
        else:
            print(f"... ¡Incorrecto, verifique! ...")
    funciones.esperarTecla()

def modificarProducto(conexionBD):
    print("\n\t\t\t...::: MODIFICAR PRODUCTO :::... \n")
    codigo = int(funciones.validacion("Código a modificar: ", r"^\d{1,10}$", "Ingrese un código válido"))
    inventario = crud.buscarCodigo(codigo, conexionBD)
    if len(inventario) > 0:
        opc = "si"
        stock=0
        while opc == "si":
            n_codigo = int(funciones.validacion("Nuevo código del producto: ", r"^\d{1,10}$", "Ingrese un código correcto (1-10 dígitos)"))
            nombre = funciones.validacion("Nombre del producto: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese un nombre válido (A-Z, máx 20 caracteres)").upper().strip()
            descripcion = funciones.validacion("Descripción: ", r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]{1,25}$", "Ingrese una descripción válida (máx 25 caracteres)").upper().strip()
            categoria = funciones.validacion("Categoría: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese una categoría válida").upper().strip()
            precioBruto = round(float(funciones.validacion("Precio bruto: ", r"^\d+(\.\d{1,5})?$", "Ingrese un valor numérico correcto")), 2)
    
        
            precioNeto = funciones.neto(precioBruto)
            t_precio = round((precioNeto * stock), 2)
        
            respuesta = crud.modificarCodigo(n_codigo, nombre, descripcion, categoria, precioBruto, precioNeto, stock, t_precio, codigo, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
        
            opc = ""
            while opc != "si" and opc != "no":
                opc = input("¿Deseas modificar otro producto? (si/no) ").lower().strip()
    else:
        print(f"... ¡Incorrecto, verifique! ...")
    funciones.esperarTecla()    
        
