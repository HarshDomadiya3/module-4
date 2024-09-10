# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 


# class class_name:
#     data member [attributes and properties]

# set:-
    # It is a parameter that is passed to methods within a class to allow access to the instance's attributes and methods.

# Example Of A Python Class :-

class Cat:
    def __init__(self, name):
        self.name = name
cat =Cat("meow")
print(cat.name) 


