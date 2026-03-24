# for loop
# food = ["burger", "pizza", "momos", "noodles"]
# whithout loop
# print(food[0])
# print(food[1])
# print(food[2])
# print(food[3])

# using loop
# for item in food:
#     print(f"Item in food is {item}")

# Using range function
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

# for i in range(len(food)):
#     print(f"item in food is: {food[i]}")
# # o/p:item in food is: burger
# item in food is: pizza
# item in food is: momos
# item in food is: noodles

food = ["burger", "pizza", "momos", "noodles"]
element_len = len(food)
print(f"Length of food items: {element_len}")

for i in food:  #for every element in list food
    print(f"Item in food: {i}")