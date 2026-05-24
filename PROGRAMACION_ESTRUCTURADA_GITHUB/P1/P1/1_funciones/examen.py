total_sueldos = 0
contador = 0

while True:

    nombre = input("Ingresa el nombre del trabajador: ")
    horas = int(input("Ingresa las horas trabajadas: "))
    sueldo_hora = float(input("Ingresa el sueldo por hora: "))

    sueldo_base = horas * sueldo_hora

    # Calcular aumento 
    match horas:
        case 10:
            aumento = sueldo_base * 0.20
        case 15:
            aumento = sueldo_base * 0.30
        case 20:
            aumento = sueldo_base * 0.15
        case _ if horas > 25:
            aumento = sueldo_base * 0.08
        case _:
            aumento = 0

    sueldo_neto = sueldo_base + aumento

  
    print("Trabajador:", nombre)
    print("Aumento: $", aumento)
    print("Sueldo neto: $", sueldo_neto)

    contador += 1
    total_sueldos += sueldo_neto

    opcion = input("\n¿Desea ingresar otro trabajador? (si/no): ")

    if opcion.lower() == "no":
        break

print("Total de trabajadores ingresados:", contador)
print("Monto total de sueldos netos: $", total_sueldos)