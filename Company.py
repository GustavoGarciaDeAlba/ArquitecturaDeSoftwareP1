import json

class Company:
    
    def __init__(self,name, clients, employees):
        self.name = name
        self.clients = clients
        self.employees = employees
    
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
    
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