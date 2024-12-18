class Employee:
    language ="py"
    salary= 1200000
    
    
    def __init__(self, name, salary, language): #dunder methods in python. __init__  which is automatically called and this method start with umderscore
        self.name= name
        self.salary= salary
        self.language= language
        print("i am creating an object")
        
    def getinfo(self):
        print(f"the language is{self.language}.the salary is {self.salary}")
    
    
    
    
    
    
aditya = Employee("aditya", 1300000,"js")#here aditya is an object
aditya.name= "aduu"
print( aditya.name,aditya.language, aditya.salary)

