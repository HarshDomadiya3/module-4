# What relationship is appropriate for Student and Person? 
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
student1=Student("harsh")
print(student1.name) 
# This demonstrates the hierarchical relationship between the Student and Person classes
# where Student inherits attributes and methods from Person and adds its own specific attributes and methods.
