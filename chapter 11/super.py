class Employee:
    def __init__(self):
       print("constructor of employee")
    a=1
class Programmer(Employee):
    def __init__(self):
       print("constructor of programmer")
    b=2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    c=3
    
# obj= Employee()
# print(obj.a)

# obj= Programmer()
# print(obj.b, obj.a)

obj= Manager()
print(obj.b,obj.c)

'''output: constructor of programmer
constructor of manager
2 3'''