class Employee:
    language ="py"
    salary= 1200000
    
    def getinfo(self):
        print(f"the language is{self.language}.the salary is {self.salary}")
    
    
    @staticmethod
    def greet():
        print("good morning")# now greet() doesn't need self object to work as it is marked static and static methods doesn't require object
        
        
harry = Employee()
harry.language= "javascript"
print(harry.language)
harry.getinfo()
# Employee.getinfo(harry)