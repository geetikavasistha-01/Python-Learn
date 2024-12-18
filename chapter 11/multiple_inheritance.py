class Employee:
    company= "ITC"
    name = "geetika"
    salary=1200000
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
class Coder:
    language= "python"
    def printlang(self):
        print(f"out of all the languages here is your language :{self.language}")
    
    

# using inheritance
class Programmer(Employee,Coder):
    company="itc infotech"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}")
        
a=Employee()
b=Programmer()

b.show()
b.showLanguage()
b.printlang()