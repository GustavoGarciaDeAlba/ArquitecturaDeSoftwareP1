import json

class Company:
    
    def __init__(self,name, clients, employees):
        self.name = name
        self.clients = clients
        self.employees = employees
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name

    def getClients(self):
        return self.clients
    
    def setClients(self,clients):
        self.clients = clients
    
    def getEmployees(self):
        return self.employees
    
    def setEmployees(self,employees):
        self.employees = employees
    
    def addEmployee(self, empleado):
        self.employees.append(empleado)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)