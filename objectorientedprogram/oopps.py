# class student:
#     name:str
#     roll_no:int
#     course:str
#     percentage:int
#     def set_student(self, name,roll_no,course,percentage):
#         # constructor initializing instance variable
#
#             self.name=name
#             self.roll_no=roll_no
#             self.course=course
#             self.percentage=percentage
#     def print_student(self):
#         print(self.name,self.roll_no,self.course,self.percentage)
# s1=student()
# s1.set_student("anu",12,"bca","98%")
# s1.print_student()
# s2=student()
# s2.set_student("manju",23,"bca","95%")
# s2.print_student()
#
#
#
class student:
    name: str
    roll_no: int
    course: str
    percentage: int

    def __init__(self, name, roll_no, course, percentage):
        # constructor initializing instance variable

        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.percentage = percentage

    def print_student(self):
        print(self.name, self.roll_no, self.course, self.percentage)


s1 = student("anu",12,"bca","98%")
s1.print_student()

# create course :c_id,c_name,c_fee