class Boleta(): # Clase "Boleta"
    def __init__(self):
        self.categoria = None
        self.horas_extras = None
        self.tardanzas = None

    def ObtenerDatosB(self): # Metodo "ObtenerDatos"
        self.categoria = input("CATEGORIA:                 ")
        self.horas_extras = float(input("HORAS EXTRAS:              "))
        self.tardanzas = float(input("TARDANZAS: (minutos)       "))

    def Sueldo_Basico(self): # Metodo "Sueldo_basico"
        self.categoria = self.categoria.upper()
        if self.categoria == "A": sb = 3000; return sb
        elif self.categoria =="B": sb = 2500; return sb
        elif self.categoria == "C": sb = 2000; return sb
        else: sb = 0; return sb

    def Descuento_Tardanzas(self): # Metodo "Descuento_tardanzas"
        dsc = ((self.Sueldo_Basico()/240)/60)*self.tardanzas; return dsc

    def Pago_Extras(self): # Metodo "Pago_extras"
            comision = (self.Sueldo_Basico()/240)*self.horas_extras; return comision

    def Sueldo_Neto(self): # Metodo "Sueldo_neto"
        total =(self.Sueldo_Basico()+self.Pago_Extras()-self.Descuento_Tardanzas()); return total
