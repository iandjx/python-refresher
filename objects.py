my_list_variable = [1, 2, 3]
print(my_list_variable)

another_list = my_list_variable
another_list.append(4)
print(another_list)
print(my_list_variable)

###

final_list = [n for n in my_list_variable]
final_list.append(5)
print(final_list)
print(my_list_variable)

###
class LotteryPlayer:
    def __init__(self):
        self.name = "Rolf"
        self.numbers = (4,1,4,2,2)

    def total(self):
        return sum(self.numbers)

player = LotteryPlayer()
print(player.total())

###
class Student:
    def __init__(self):
        self.name = "John"
        self.school = "Harvard"

my_student_variable = Student()
print(my_student_variable)
print(my_student_variable.name)
print(my_student_variable.school)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school

# Student()
another_student = Student("Rolf", "MIT")
print(another_student)
print(another_student.name)
print(another_student.school)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

anna = Student("Anna", "Oxford")
# print(anna.marks)
anna.marks.append(56)
anna.marks.append(99)
print(anna.marks)
#
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


anna = Student("Anna", "Oxford")
# print(anna.marks)
anna.marks.append(56)
anna.marks.append(99)
print(anna.marks)
print(anna.average())