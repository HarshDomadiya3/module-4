# What relationship is appropriate for Course and Faculty?
class Faculty:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, title, faculty):
        self.title = title
        self.faculty = faculty 


professor = Faculty("harsh")
course = Course("Computer", professor)

print(course.title ,course.faculty.name)



# The Course class has a faculty attribute to store the Faculty object that teaches the course.
# The Faculty class has a courses attribute to store a list of Course objects that the faculty teaches.
