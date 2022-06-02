import json

class Client:
    
    def __init__(self,name, company, age, phone):
        self.name = name
        self.company = company
        self.age = age
        self.phone = phone
    
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
    
    def getPhone(self):
        return self.phone
    
    def setPhone(self,phone):
        self.phone = phone