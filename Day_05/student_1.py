class Student:

    # Important detail (very useful for interviews):
    # __init__ is NOT the real constructor
    # Real constructor is __new__ (rarely used)
    # __new__ is rarely used because object creation is already handled by Python internally,
    # and most developers only need to initialize data, not control object creation.

    def __new__(cls):
        print("new is real constructor used for creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")


s1 = Student()

# #o/p:
# Creating object
# Initializing object
