from Empleado import Empleado

class Directivo(Empleado):

    def __init__(self,nombre, empresa, edad, sueldo, categoria, subordinados):
        super().__init__(nombre, empresa, edad, sueldo)
        self.categoria = categoria
        self.subordinados = subordinados
    
    def getCategoria(self):
        return self.categoria
    
    def setCategoria(self,categoria):
        self.categoria = categoria
    
    def getSubordinados(self):
        return self.subordinados
    
    def setSubordinados(self,subordinados):
        self.subordinados = subordinados
    
    def mostrarInfo(self):
        pass