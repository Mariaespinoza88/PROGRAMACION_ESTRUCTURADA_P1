
import funciones
from movimientos import crud

def agregarMovimiento(conexionBD):
    print("\n\t\t\t...::: AGREGAR MOVIMIENTO :::... \n")
    opc = "si"
    while opc == "si":
        nombre = funciones.validacion("Nombre del producto: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese un nombre válido").upper().strip()
        producto = crud.buscarNombre(nombre, conexionBD)    
        if len(producto) > 0:
            codigo = producto[0][0]
            cantidad = int(funciones.validacion("Cantidad: ", r"^\d{1,10}$", "Ingrese una cantidad numérica correcta"))
            tipo = funciones.validacion("Tipo de movimiento (Entrada/Salida): ", r"^[a-zA-Z]{1,7}$", "Ingrese un valor válido (Entrada/Salida)").upper().strip()

            if crud.insertar(codigo, nombre, cantidad, tipo, conexionBD):
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
        else:
            print(f"\n\t... ¡El producto {nombre} no existe en la base de datos! ...")
        
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("\n¿Deseas agregar otro movimiento? (si/no) ").lower().strip()
    funciones.esperarTecla()

def mostrarMovimiento(conexionBD):
    print("\n\t\t...:::: MOSTRAR MOVIMIENTOS ::::...\n")
    inventario = crud.consultar(conexionBD)
    if len(inventario) > 0:
        print(f"\t{'ID':<5}\t{'Código':<10}\t{'Nombre':<15}\t{'Cantidad':<10}\t{'Tipo':<10}\n")
        print("-" * 75)
        for i in inventario:
            print(f"\t{i[0]:<5}\t{i[1]:<10}\t{i[2]:<15}\t{i[3]:<10}\t{i[4]:<10}")
        print("-" * 75)
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("\n¿Deseas generar un reporte en PDF? (Si/No) ").lower().strip()      
            if opc == "si":
                funciones.generarPDF(inventario)
    else:
        print("...¡No hay movimientos registrados para mostrar!...")
    funciones.esperarTecla()

def limpiarMovimiento(conexionBD):
    print("\n\t\t\t...::: BORRAR TODOS LOS MOVIMIENTOS :::... \n")
    opc = ""
    while opc != "si" and opc != "no":
        opc = input("¿Estás seguro que deseas borrar TODOS los movimientos (si/no)? ").lower().strip()
    if opc == "si":
        if crud.vaciar(conexionBD):
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    funciones.esperarTecla()

def buscarMovimiento(conexionBD):
    print("\n\t\t\t...::: BUSCAR MOVIMIENTO :::... \n")
    opc = "si"
    while opc == "si":
        id_movimiento = int(funciones.validacion("Número de ID del movimiento: ", r"^\d{1,10}$", "Ingrese un ID válido"))
        resultado = crud.buscar(id_movimiento, conexionBD)
        if len(resultado) > 0:
            print(f"\t{'ID':<5}\t{'Código':<10}\t{'Nombre':<15}\t{'Cantidad':<10}\t{'Tipo':<10}\n")
            print("-" * 75)
            for i in resultado:
                print(f"\t{i[0]:<5}\t{i[1]:<10}\t{i[2]:<15}\t{i[3]:<10}\t{i[4]:<10}")
            print("-" * 75)
        else:
            print(f"\n\t... ¡No existe el movimiento con ID {id_movimiento}, verifique! ...")
            
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("\n¿Deseas buscar otro movimiento? (Si/No) ").lower().strip()
    funciones.esperarTecla()

def borrarMovimiento(conexionBD):
    print("\n\t\t\t...::: BORRAR MOVIMIENTO :::... \n")
    id_movimiento = int(funciones.validacion("Número de ID del movimiento: ", r"^\d{1,10}$", "Ingrese un ID válido"))
    resultado = crud.buscar(id_movimiento, conexionBD)
    if len(resultado) > 0:
        print(f"\t{'ID':<5}\t{'Código':<10}\t{'Nombre':<15}\t{'Cantidad':<10}\t{'Tipo':<10}\n")
        print("-" * 75)
        for i in resultado:
            print(f"\t{i[0]:<5}\t{i[1]:<10}\t{i[2]:<15}\t{i[3]:<10}\t{i[4]:<10}")
        print("-" * 75)
        
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Estás seguro que deseas borrar el movimiento (Si/No)? ").lower().strip()
            if opc == "si":
                if crud.eliminar(id_movimiento, conexionBD):
                    funciones.accionExitosa()
                else:
                    funciones.accionNoExitosa()
    else:
        print(f"... ¡Movimiento {id_movimiento} no existe, verifique! ...")
    funciones.esperarTecla()

def modificarMovimiento(conexionBD):
    print("\n\t\t\t...::: MODIFICAR MOVIMIENTO :::... \n")
    id_movimiento = int(funciones.validacion("Número de ID del movimiento: ", r"^\d{1,10}$", "Ingrese un ID válido"))
    inventario = crud.buscar(id_movimiento, conexionBD)
    if len(inventario) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Estás seguro que deseas modificar el movimiento (Si/No)? ").lower().strip()
            if opc == "si":
                cantidad = int(funciones.validacion("Nueva cantidad: ", r"^\d{1,10}$", "Ingrese una cantidad numérica"))
                tipo = funciones.validacion("Tipo de movimiento (Entrada/Salida): ", r"^[a-zA-Z]{1,7}$", "Ingrese un tipo válido").upper().strip()
                if crud.modificar(id_movimiento, cantidad, tipo, conexionBD):
                    funciones.accionExitosa()
                else:
                    funciones.accionNoExitosa()
    else:
        print(f"... ¡El movimiento {id_movimiento} no existe, verifique! ...")
    funciones.esperarTecla()


