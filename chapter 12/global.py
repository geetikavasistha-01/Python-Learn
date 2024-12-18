a = 89

def fun(): 
    global a #changed the global keyword
    a = 3
    print(a)


fun()
print(a)