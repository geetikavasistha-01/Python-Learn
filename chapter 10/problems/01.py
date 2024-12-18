class Programmer:
    company="microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary= salary
        self.pin= pin
        
p= Programmer("geetika",1200000,2319)
print(p.salary,p.name,p.pin)
r= Programmer("aditya",1200000,2827)
print(r.salary,r.name,r.pin)

     