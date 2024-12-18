def goodDay(name,ending):
    print("good, " + name)
    print(ending)
    
goodDay("harry" , "thankyou")
goodDay("rohan" ,"thanks")
goodDay("divya" ," thanks")



#returning a value to any variable whol asks it while calling
def goodDay(name,ending):
    print("good, " + name)
    print(ending)
    return "done"
    
a=goodDay("harry" , "thankyou")
print(a)
