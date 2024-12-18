class Employee:
    a=1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3
    
obj= Employee()
print(obj.a)

obj= Programmer()
print(obj.b, obj.a)

obj= Manager()
print(obj.b,obj.c)