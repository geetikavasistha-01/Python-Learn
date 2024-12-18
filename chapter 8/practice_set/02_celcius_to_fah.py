# c/5= (f-32)/9
# c= 5* (f-32)/9

def f_to_c(f):
    return 5*(f-32)/9
f= int(input("enter temp in F"))
c= f_to_c(f)
print(f"{round(c,2)} °C ")

# to prevent a new line at the end in the print fuction is by using end=""