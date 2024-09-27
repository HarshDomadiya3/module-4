# What relationship is appropriate for Course and Faculty?
class Course:
    def __init__(self,name):
        self.name=name
        self.faculty=[]
class Faculty:
    def __init__(self,name):
        self.name=name
course1=Course("Introdction to Python")
course1.faculty.append(Faculty("harsh"))
course1.faculty.append(Faculty("domadiya"))
faculty1=Faculty("name")
faculty1.courses=[course1] 

# The Course class has a faculty attribute to store the Faculty object that teaches the course.
# The Faculty class has a courses attribute to store a list of Course objects that the faculty teaches.
