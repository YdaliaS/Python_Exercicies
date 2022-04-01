from trabajador import Trabajador

# Clase Hijo
class Boleta(Trabajador): # Clase "Boleta"
    # Metodos
    def Sueldo_Basico(self): # Metodo "Sueldo_basico"
        if self.categoria == "A" or self.categoria == "a":
            sb = 3000
            return sb
        elif  self.categoria =="B" or self.categoria == "b":
            sb = 2500
            return sb
        elif self.categoria == "C" or self.categoria == "c":
            sb = 2000
            return sb
        else:
            sb = 0
            return sb

    def Descuento_Tardanzas(self): # Metodo "Descuento_tardanzas"
        dsc = ((self.Sueldo_Basico()/240)/60)*self.tardanzas
        return dsc

    def Pago_Extras(self): # Metodo "Pago_extras"
            comision = (self.Sueldo_Basico()/240)*self.horas_extras
            return comision

    def Sueldo_Neto(self): # Metodo "Sueldo_neto"
        total =(self.Sueldo_Basico()+self.Pago_Extras()-self.Descuento_Tardanzas())
        return total