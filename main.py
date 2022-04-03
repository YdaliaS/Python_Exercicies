from trabajador import Trabajador
from boleta import Boleta
import os
import time

Boleta1 = Boleta()
Trabajador1 = Trabajador()
os.system("cls")

Trabajador1.ObtenerDatosT();Boleta1.ObtenerDatosB()

if Boleta1.Sueldo_Basico() > 0:

    espacios = " "
    for i in range(5):
        print(" PROCESANDO BOLETA DE PAGO...".format(espacios))
        espacios+= " "; time.sleep(0.3); os.system("cls")

    Trabajador1.Imprimir()
    print("    CATEGORIA:           ",Boleta1.categoria)
    print("    HORAS EXTRAS:        ",Boleta1.horas_extras)
    print("    TARDANZAS:(minutos)  ",Boleta1.tardanzas)
    print("__________________________________")
    print("      ______________________      ")
    print("     |                      |     ")
    print("     |    FERROTEK  S.A.C   |     ")
    print("     |______________________|     ")
    print("                                  ")
    print("      *** BOLETA DE PAGO ***      ")
    print("                                  ")
    print("    NOMBRE:              ", Trabajador1.trabajador.title())
    print("    CATEGORIA:           ", Boleta1.categoria.upper())
    print("    SUELDO BASICO:       ", Boleta1.Sueldo_Basico())
    print("    DESCUENTO TARDANZAS: ", round(Boleta1.Descuento_Tardanzas(), 2))
    print("    PAGO HORAS EXTRAS:   ", round(Boleta1.Pago_Extras(), 2))
    print("    SUELDO NETO:         ", round(Boleta1.Sueldo_Neto(), 2))
    print("                                   ")
    print("___________________________________")

    input("PRESIONE ENTER PARA SALIR...")
    print("\nGracias por su preferencia, regrese pronto")
else:
    print("CATEGORIA NO ENCONTRADA!!!")
    input("PRESIONE ENTER PARA SALIR...")
