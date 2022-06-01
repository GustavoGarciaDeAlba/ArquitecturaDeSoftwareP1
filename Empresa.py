class Empresa:
    
    def __init__(self,nombre, clientes, empleados):
        self.nombre = nombre
        self.clientes = clientes
        self.empleados = empleados
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre = nombre

    def getClientes(self):
        return self.clientes
    
    def setClientes(self,clientes):
        self.clientes = clientes
    
    def getEmpleados(self):
        return self.empleados
    
    def setEmpleados(self,empleados):
        self.empleados = empleados
    