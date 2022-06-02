import json
from Employee import Employee

class Directive(Employee):

    def __init__(self,name, company, age, salary, category, subordinates):
        super().__init__(name, company, age, salary, True)
        self.category = category
        self.subordinates = subordinates
    
    def getCategory(self):
        return self.category
    
    def setCategory(self,category):
        self.category = category
    
    def getSubordinates(self):
        return self.subordinates
    
    def setSubordinates(self,subordinates):
        self.subordinates = subordinates
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
