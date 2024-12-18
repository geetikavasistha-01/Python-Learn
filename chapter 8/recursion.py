# factorial(n)= n*factorial(n-1)
''' 
ex:- factorail(3)= 3* (3-1)
3*2*(2-1)= 3*2*1= 6
'''

def factorial(n):
    if(n==1 or n==0):
       return 1
    return n *factorial(n-1)

n= int(input("enter anumber"))
print(f"the factorial of this number is: {factorial(n)}")    

