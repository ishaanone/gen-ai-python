# #-----------for loop---------111111111111----------
food = ["burger", "pizza", "momos", "noodles"]
# whithout loop
print(food[0])
print(food[1])
print(food[2])
print(food[3])

# # using loop---------------22222222222-----------
# for item in food:
#     print(f"Item in food is {item}")

# #o/p:Item in food is burger
# Item in food is pizza
# Item in food is momos
# Item in food is noodles

# # Using range function-------------333333333--------
# for i in range(10):
#     print(f"item is: {i}")

# #o/p:item is: 0
# item is: 1
# item is: 2
# item is: 3
# item is: 4
# item is: 5
# item is: 6
# item is: 7
# item is: 8
# item is: 9

# # ------------44444444444444444444---------------------------
# for i in range(len(food)):
#     print(f"item in food is: {food[i]}")

# # o/p:item in food is: burger
# item in food is: pizza
# item in food is: momos
# item in food is: noodles

# food = ["burger", "pizza", "momos", "noodles"]
# element_len = len(food)
# print(f"Length of food items: {element_len}")

# #----------------555555555555555555555-------------------------
# for i in food:  # for every element in list food
#     print(f"Item in food: {i}")

# #o/p:Item in food: burger
# Item in food: pizza
# Item in food: momos
# Item in food: noodles

# #------------------66666666666666666666666------------------------
# method 2 using range function
# for i in range(element_len):  # for every element in range 4-> i-0, i-1, i-2, i-3
#     print(f"here is element: {food[i]}")

# #o/p:here is element: burger
# here is element: pizza
# here is element: momos
# here is element: noodles

# #-----------------777777777777777777777777---------------------------
# # lets say i want to only print second and third value
# for i in range(1, 3):
#     print(f"Here is two food i like:: {food[i]}")

# #o/p:Here is two food i like:: pizza
# Here is two food i like:: momos

# #------------------------888888888888888888888888888888--------------
# SUPPOSE WE ARE DEALING WITH THE STRING
# name = input("what is your name: ")
# # method1 without loop
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

# # o/p:what is your name: ishaan
# i
# s
# h
# a
# a
# n
# #---------------999999999999----negative scenario
# name = input("Enter your name: ")
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])

# # o/p: IndexError: string index out of range at print(name[6]), make sure input value is ishaan

# # method2 using loop----------------10101010101010101010-----------------
# for i in name:  # for every element in the name
#     print(i)
# #o/p:Enter your name: ishaan
# i
# s
# h
# a
# a
# n
