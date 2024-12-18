class Employee:
    company= "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company ="ITC infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
    
#     def showlanguage(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")


# using inheritance
class Programmer(Employee):
    company="itc infotech"
    def showLnaguage(self):
        print(f"the name is {self.name} and he is good with {self.language}")


a=Employee()
b=Programmer()
print(a.company,b.company) 