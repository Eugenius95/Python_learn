#example of creating a tuple
thistuple = ("Apple", "banana", "cherry","apple", "Cherry")
print(thistuple)

#Creating a tuple for students in a classroom

grade_1 = ("Lesego", "Palesa", "Lesiba", "Xolani", "Gift")
print(grade_1)

#Vehicle example

brand = ("Bmw", "Benz", "Fiat")
print(brand)

#tuple with  different data type
tuple_st = ("Wena", "Rona", "Bona", "Lena")
tuple_int = (1, 2, 3 , 4, 5, 6)
tuple_bolean = (True, False, False, True)
print(tuple_bolean)
print(tuple_int)
print(tuple_st)

#Access tuple items
#Tuples are unchangeabl;e,immutable
print(tuple_st[2])
print(tuple_int[1:3])

#convert tuple to a list
list_tuple = list(tuple_st) #creat a list name
list_tuple[0] = "people" #add a new item on the newly created list
tuple_st = tuple(list_tuple) #upfate tuple from the original tuple
print(tuple_st)

vehicle_list = list(brand)
vehicle_list[2] = "Peugeot"
brand = tuple(vehicle_list)
print(brand)

