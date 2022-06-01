class Cliente:
    
    def __init__(self,nombre, empresa, edad, telefono):
        self.nombre = nombre
        self.empresa = empresa
        self.edad = edad
        self.telefono = telefono
    
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
    
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self,telefono):
        self.telefono = telefono