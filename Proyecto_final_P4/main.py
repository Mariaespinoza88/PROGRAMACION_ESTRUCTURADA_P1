'''
Proyecto de control de inventarios, que incluye dos tablas de base de datos, para poder registrar los productos, así como su entrada y salida.
Debe de incluir:
1.- 20 expresiones algoritmicas, respetando la jerarquia de operaciones
2.- 2 constantes y 10 variables
3.- Contadores y acumuladores
4.- Estructuras de control y repeticion
5.- Listas y diccionarios
6.- Generar archivo 
7.- Validación "RegEx"

'''
import funciones
from productos import productos
from movimientos import movimientos

conexionBD = funciones.conectar()
inventario=[]
opc="1"


while opc!="3":
    funciones.borrarPantalla()
    opc = funciones.menuPrincipal()
    match opc:
        case "1":
                opc=""
                while opc!="7":
                        funciones.borrarPantalla()
                        opc=funciones.menuSecundario()

                        match opc:
                                case "1":
                                        funciones.borrarPantalla()
                                        productos.agregarProducto(conexionBD)
                                case "2":
                                        funciones.borrarPantalla()
                                        productos.borrarProducto(conexionBD)
                                case "3":
                                        funciones.borrarPantalla()
                                        productos.modificarProducto(conexionBD)
                                case "4":
                                        funciones.borrarPantalla()
                                        productos.mostrarProductos(conexionBD)
                                case "5":
                                        funciones.borrarPantalla()
                                        productos.buscarProducto(conexionBD)
                                case "6":
                                        funciones.borrarPantalla()
                                        productos.limpiarProducto(conexionBD)
                        
                                case "7":
                                        funciones.borrarPantalla()
                        
                                case _:
                                        funciones.opcionInvalida()
        case "2":
                opc=""
                while opc !="7":
                        funciones.borrarPantalla()
                        opc=funciones.menuSecundario()
                        match opc:
                        
                                case "1":
                                        funciones.borrarPantalla()
                                        movimientos.agregarMovimiento(conexionBD)
                                case "2":
                                        funciones.borrarPantalla()
                                        movimientos.borrarMovimiento(conexionBD)
                                case "3":
                                        funciones.borrarPantalla()
                                        movimientos.modificarMovimiento(conexionBD)
                                case "4":
                                        funciones.borrarPantalla()
                                        movimientos.mostrarMovimiento(conexionBD)                                
                                case "5":
                                        funciones.borrarPantalla()
                                        movimientos.buscarMovimiento(conexionBD)
                                case "6":
                                        funciones.borrarPantalla()
                                        movimientos.limpiarMovimiento(conexionBD)
                        
                                case "7":
                                        funciones.borrarPantalla()
                        
                                case _:
                                        funciones.opcionInvalida()
        case "3":
                funciones.borrarPantalla()
                funciones.terminarPrograma()

        case _:
                funciones.opcionInvalida()
