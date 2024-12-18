# # remove function

# def rem(l, word):
#     for item in l:
#          l.remove(word)
#          return l
# l=["harry","aditya","dudu","geet","beet"]
# print(rem(l,"geet"))




# strip function
def rem(l, word):
    n=[]
    for item in l:
         if not(item==word):
             n.append(item.strip(word))
         return n
l=["harry","aditya","dudu","geet","beet"]
print(rem(l,"eet"))