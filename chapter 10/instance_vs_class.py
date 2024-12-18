class Employee:
    language ="py"
    salary= 1200000
    
harry = Employee()
harry.language= "javascript"
print(harry.language) #op:javascript
    
# instance attribute take prefrence over class attribute during assignment and retrieval