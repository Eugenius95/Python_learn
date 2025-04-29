#classes and objects
#class its a blueprint or template
n = input("Name: ")
a = input("Age: ")
m = input("Marks: ")

class student:
    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.marks = m
        
    def display(self):
        print("Hi", self.name)
        print("Your age", self.age)
        print("Your marks", self.marks)
        
s1 = student(n, a, m)
s1.display()

#arguments passing to the parameters


             
        