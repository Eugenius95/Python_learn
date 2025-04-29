class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def myfunc(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

p1 = Person("John Doe", 36, "New York")
p1.myfunc()
