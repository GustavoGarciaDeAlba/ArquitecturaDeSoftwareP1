import json
from pymongo import MongoClient
from bson import ObjectId

from Client import Client
from Directive import Directive
from Employee import Employee
from Company import Company


class App:

    def __init__(self):
        self.DB = MongoClient("mongodb+srv://jesus:cisco@arquitecturadesoftware.ddie5.mongodb.net/?retryWrites=true&w=majority").arquitecturadesoftware
        self.COMPANIES = self.getCompaniesFromDB()

    def run(self):
        while True:
            self.menu()
            option = int(input("Enter an option: "))
            if option == 1:
                self.registerCompany()
            elif option == 2:
                self.showCompaniesData()
            else:
                print("Invalid option")

    def menu(self):
        print("""
        ============Menu===================\n
            1. Register Company
            2. Show Company Data\n
        """)
    
    def getCompaniesFromDB(self):
        companies = self.DB.companies.find({})
        return companies
    
    def showCompaniesData(self):
        COMPANIES = self.getCompaniesFromDB()
        for company in COMPANIES:
            company = json.loads(JSONEncoder().encode(company))
            print("======",company["name"], "======")
            print("\nEMPLOYEES: ")
            print(company["employees"])
            print("\nCLIENTS: ")
            print(company["clients"])

    def registerCompany(self):
        companyName = input("Enter the name of the company: ")
        employees = self.registerEmployees(companyName)
        clients = self.registerClients(companyName)
        newCompany = Company(companyName, clients, employees)
        self.DB.companies.insert_one(newCompany.__dict__)
        return newCompany
    
    def registerEmployees(self, company):
        employees = []
        while True:
            employees.append(self.registerEmployee(company).__dict__)
            if int(input("Do you want to add another employee? (1. Yes, 2. No): ")) == 2:
                break
        return employees

    def registerClients(self, company):
        clients = []
        while True:
            clients.append(self.registerClient(company).__dict__)
            if int(input("Do you want to add another client? (1. Yes, 2. No): ")) == 2:
                break
        return clients

    def registerEmployee(self, company):
        name = input("Enter the name of the employee: ")
        age = input("Enter the age of the employee: ")
        salary = input("Enter the salary of the employee: ")
        isDirective = int(input("Enter the type of the employee (1. Directive, 2. Employee): ")) == 1
        if isDirective:
            category = input("Enter the category of the directive: ")
            print("Register subordinates: ")
            subordinates = self.registerEmployees(company)
            employee = Directive(name, company, age, salary, category, subordinates)
            self.DB.directives.insert_one(employee.__dict__)
        else:
            employee = Employee(name, company, age, salary, isDirective)
            self.DB.employees.insert_one(employee.__dict__)

        return employee

    def registerClient(self, company):
        name = input("Enter the name of the client: ")
        age = input("Enter the age of the client: ")
        phone = input("Enter the phone of the client: ")
        client = Client(name, company, age, phone)

        self.DB.clients.insert_one(client.__dict__)

        return client

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = App()
app.run()
