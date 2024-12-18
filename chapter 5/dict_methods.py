marks= {
    "geetika" : 100,
    "aditya" : 90,
    "avi" : 77,
    "taylor": 100
}
print(marks.items())# RETURNS A LIST OF KEY VALUE TUPLES
marks.keys()# return a list containing dictionary's keys
print(marks.keys())


marks. update({"friends" : 77 })
print(marks)

# print(marks.get("mere") )  # prints none
# print(marks["mere"]) #retuns an error

ke = ['a','b','c']
# new_dict = dict.fromkeys(keys, 0)
# print(new_dict)


print(ke.pop('a'))