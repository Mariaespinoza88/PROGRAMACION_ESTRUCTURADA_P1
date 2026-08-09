import mysql.connector
import re
from fpdf import FPDF
from datetime import datetime


IVA = 0.16
DESCUENTO_MAYOREO = 0.05

def validacion(texto, validacion_regex, mensaje):
    opc = True
    entrada = ""
    while opc:
        entrada = input(texto).strip()
        if re.match(validacion_regex, entrada):
            opc = False
        else:
            print(mensaje)
    return entrada

def neto(preciobruto):
    precioneto = preciobruto * (1 + IVA)
    return round(precioneto, 2)

def esperarTecla():
    input("\n\t\t\t🔄🔄¡Oprima cualquier tecla para continuar!🔄🔄")

def opcionInvalida():
    input("\n\t\t\t❌❌¡Opción invalida, por favor verifique!❌❌")

def accionExitosa():
    input("\n\t\t\t🎉🎉¡Acción realizada con éxito!🎉🎉")

def accionNoExitosa():
    input("\n\t\t\t🚨🚨¡No fue posible realizar esta acción, intentalo mas tarde!🚨🚨")

def terminarPrograma():
    input("\n\t\t\t...::🙏  GRACIAS POR UTILIZAR NUESTRO SISTEMA 🙏 ::...\n\t\t\t\t\t..✨ VUELVA PRONTO ✨..\n")

def borrarPantalla():
    print("\033c")

def menuPrincipal():
    print("\n\t\t\t\t\t...:::: M E N Ú ::::...\n")
    opcion = input("\n\t1.- Productos \n\t2.- Movimientos de producto\n\t3.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion

def menuSecundario():
    print("\n\t\t\t\t...:::: I N V E N T A R I O ::::...\n")
    opcion = input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Regresar\n\t\tEscribe una opción: ").strip()
    return opcion

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_inventarios"
        ) 
        return conexion
    except:
        input("...¡Por el momento no es posible conectar el sistema con la Base de datos!...")
        return None

def generarPDF(datos):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(190, 10, "REPORTE DE MOVIMIENTOS", ln=True, align="C")
    pdf.ln(5)


    pdf.set_font("Arial", "B", 10)
    pdf.cell(20, 8, "ID", border=1)
    pdf.cell(35, 8, "Código", border=1)
    pdf.cell(55, 8, "Nombre", border=1)
    pdf.cell(40, 8, "Tipo", border=1)
    pdf.cell(40, 8, "Cantidad", border=1)
    pdf.ln()

    pdf.set_font("Arial", "", 10)
    for fila in datos:
        pdf.cell(20, 8, str(fila[0]), border=1)
        pdf.cell(35, 8, str(fila[1]), border=1)
        pdf.cell(55, 8, str(fila[2]), border=1)
        pdf.cell(40, 8, str(fila[3]), border=1)
        pdf.cell(40, 8, str(fila[4]), border=1)
        pdf.ln()

    nombre = "Reporte_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".pdf"
    pdf.output(nombre)
    print(f"\nReporte generado correctamente: {nombre}")

def productosPDF(datos):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(190, 10, "REPORTE DE PRODUCTOS", ln=True, align="C")
    pdf.ln(5)


    pdf.set_font("Arial", "B", 10)
    pdf.cell(20, 8, "Codigo", border=1)
    pdf.cell(35, 8, "Nombre", border=1)
    pdf.cell(55, 8, "Descripción", border=1)
    pdf.cell(20, 8, "Categoria", border=1)
    pdf.cell(15, 8, "P. Bruto", border=1)
    pdf.cell(15, 8, "P. Neto", border=1)
    pdf.cell(15, 8, "Stock", border=1)
    pdf.cell(15, 8, "P. Total", border=1)
    pdf.ln()

    pdf.set_font("Arial", "", 10)
    for fila in datos:
        pdf.cell(20, 8, str(fila[0]), border=1)
        pdf.cell(35, 8, str(fila[1]), border=1)
        pdf.cell(55, 8, str(fila[2]), border=1)
        pdf.cell(20, 8, str(fila[3]), border=1)
        pdf.cell(15, 8, str(fila[4]), border=1)
        pdf.cell(15, 8, str(fila[5]), border=1)
        pdf.cell(15, 8, str(fila[6]), border=1)
        pdf.cell(15, 8, str(fila[7]), border=1)
        pdf.ln()

    nombre = "Reporte_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".pdf"
    pdf.output(nombre)
    print(f"\nReporte generado correctamente: {nombre}")

