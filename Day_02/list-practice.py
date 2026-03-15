## List

# groceries = ["Biscuits", "bread", "milk", "butter", "soap", "toothpaste"]
# print(groceries)
# print(groceries[0])
# print(groceries[1])
# print(groceries[2])
# print(groceries[3])
# print(groceries[4])
# print(groceries[5])

## list allows duplicate values and different datatype in the string
# fruits = ["banana", "cherry", "cherry", True, 40]
# print(fruits)

## Length of list
# we will use len() function
# print(len(fruits))
# print(f"Data type of fruits is: {type(fruits)}")  # tells what is datatype of fruits

## range of indexes
fruits = ["banana", "apple", "cherry", "pineapple", "strawberry"]
# return third, fourth and fifth items
print(f"return third, fourth and fifth items: {fruits[2:5]}")   # last index is excluded, and it is 0-based index
print(f"return first and second items: {fruits[:2]}")
print(f"return everything from third item: {fruits[2:]}")
