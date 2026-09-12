from abc import ABC, abstractmethod

class person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def role_info(self):
        pass
    def __str__(self):
        return self.name + " - " + self.email

class studnet(person):
    def __init__(self, name, email, studnet_id):
        super().__init__(name, email)
        self.studnet_id = studnet_id
    def role_info(self):
        return "Student: " + self.name

class lecturer(person):
    def role_info(self):
        return "Lecturer: " + self.name

class course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def show_students(self):
        for student in self.students:
            print(student)

# Craeting objects
s1 = studnet("Ahmad", "ahmad@gmail.com", 101)
s2 = studnet("Ali", "ali@gmail.com", 102)

teacher = lecturer("Mr Karim", "karim@gmail.com")

course = course("Python")

course.add_student(s1)
course.add_student(s2)

people = [s1, teacher]

for person in people:
    print(person.role_info())

print("\ncourse: " , course.course_name)
course.show_students()