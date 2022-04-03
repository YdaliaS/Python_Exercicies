class Trabajador(): # Clase "Trabajador"
    def __init__(self):
        self.trabajador = None

    #Metodos
    def ObtenerDatosT(self): # Metodo "ObtenerDatos"
        print("__________________________________")
        print("      ______________________      ")
        print("     |                      |     ")
        print("     |    FERROTEK  S.A.C   |     ")
        print("     |______________________|     ")
        print("                                  ")
        print("      *** DATOS DE ENTRADA ***    ")
        print("                                  ")
        self.trabajador = input("TRABAJADOR:                ")

    def Imprimir(self):
        print("__________________________________")
        print("      ______________________      ")
        print("     |                      |     ")
        print("     |    FERROTEK  S.A.C   |     ")
        print("     |______________________|     ")
        print("                                  ")
        print("      *** DATOS DE ENTRADA ***    ")
        print("                                  ")
        print("    NOMBRE:              ",self.trabajador)
