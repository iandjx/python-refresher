# class Student:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []
#
#     def average(self):
#         return sum(self.marks) / len(self.marks)
#
#     @classmethod
#     def friend(cls, origin, friend_name, salary):
#         return cls(friend_name, origin.school, salary)
#
#
# # anna = Student("Anna", "Oxford")
#
#
# # friend = anna.friend("Greg")
# # friend = Student.friend(anna, "Greg")
# # print(friend.name)
# # print(friend.school)
#
#
# ###
#
# class WorkingStudent(Student):
#     def __init__(self, name, school, salary):
#         super().__init__(name, school)
#         self.salary = salary
#
#
# rolf = WorkingStudent("Rolf", "Harvard", 20.00)
# print(rolf.salary)
# sue = Student.friend(rolf, "sue", 123)
# print(sue.salary)  # Error!
#

###

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school,*args, **kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


rolf = WorkingStudent("Rolf", "Harvard", 20.00, "engineer")
sue = WorkingStudent.friend(rolf, "Sue", 15.00, "blah")
print(sue.salary)  # This works!
print(sue.job_title)

ian = WorkingStudent.friend(rolf, "ian",  salary=202, job_title="yolo")
print(ian.job_title)