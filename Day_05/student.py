class Student:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_detail(self):
        return f"name: {self.name}, age: {self.age}"


s1 = Student("Ishaan", 25)
# s1.name = "Ishaan"F
# s1.age = 36
print(s1.student_detail())
