class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks =[]

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school")

anna = Student("anna", 'MIT')
rolf = Student("rolf", 'oxford')
anna.marks.append(56)
anna.marks.append(61)
Student.go_to_school()
