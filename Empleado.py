class Empleado:

    def __init__(self,nombre, empresa, edad, sueldo, esDirectivo):
        self.nombre = nombre
        self.empresa = empresa
        self.edad = edad
        self.sueldo = sueldo
        self.esDirectivo = esDirectivo

    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def getEmpresa(self):
        return self.empresa
    
    def setEmpresa(self,empresa):
        self.empresa =empresa

    def getEdad(self):
        return self.edad

    def setEdad(self,edad):
        self.edad = edad
    
    def getSueldo(self):
        return self.sueldo
    
    def setSueldo(self,sueldo):
        self.sueldo = sueldo
    
    def getEsDirectivo(self):
        return self.esDirectivo
    
    def setEsDirectivo(self,esDirectivo):
        self.esDirectivo = esDirectivo