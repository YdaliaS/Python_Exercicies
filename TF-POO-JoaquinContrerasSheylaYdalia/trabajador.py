class Trabajador(): # Clase "Trabajador"
    def __init__(self):
        self.trabajador = None
        self.categoria = None
        self.horas_extras = None
        self.tardanzas = None

    #Metodos
    def ObtenerDatos(self): # Metodo "ObtenerDatos"
        self.trabajador = input("TRABAJADOR:                ")
        self.categoria = input("CATEGORIA:                 ")
        self.horas_extras = float(input("HORAS EXTRAS:              "))
        self.tardanzas = float(input("TARDANZAS: (minutos)       "))