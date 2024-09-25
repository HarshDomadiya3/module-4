#  Explain Inheritance in Python with an example .What is init? Or What Is A Constructor In Python? 

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("animal sound")
class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
animal1 =Animal("Animal")
dog1 =Dog("Buddy")
cat1 =Cat("Whiskers")
animal1.speak()
dog1.speak()
cat1.speak()

#  __init__ :- is a special method known as the constructor. It is used to initialize the attributes of a class when an instance (object) of the class is created.

# constructor :- is a special method used to initialize a newly created object. The constructor method in Python is named __init__. When you create an instance of a class, the __init__ method is automatically called to set up the initial state of the object.
