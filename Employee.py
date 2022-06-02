import json

class Employee:

    def __init__(self,name, company, age, salary, isDirective):
        self.name = name
        self.company = company
        self.age = age
        self.salary = salary
        self.isDirective = isDirective

    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
    def getCompany(self):
        return self.company
    
    def setCompany(self,company):
        self.company =company

    def getAge(self):
        return self.age

    def setAge(self,age):
        self.age = age
    
    def getSalary(self):
        return self.salary
    
    def setSalary(self,salary):
        self.salary = salary
    
    def getIsDirective(self):
        return self.isDirective
    
    def setIsDirective(self,isDirective):
        self.isDirective = isDirective
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)