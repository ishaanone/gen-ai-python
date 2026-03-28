#### Animal website using class


class animal:
    def __init__(self, animaltype):  # constuctor will be executed by default
        print(f"You selected the animal: {animaltype}")

# 👉 Use .lower() or .casefold() to perform case-insensitive string comparison in Python.
        if animaltype == "Dog":
            print("We have 2 variety of dogs . Which one you want?")
            x = int(input("Select 1 for lABRADOR And 2 for Husky "))
            # after user selects whether they want labrador or husky ..i want to run a method to find the pricing
            self.dogcost(x)  # calling method
        else:
            print("we only have dogs")

    def dogcost(self, x):
        if x == 1:
            print("Pricing will be between $100 to your complete life earning")
        else:
            print("Pricing will be $10000 to $30000")


a = input("You want Dog or other animal? ")
d1 = animal(a)
