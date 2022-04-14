# 20CS010 - Meet Butani
# Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student
# class has data members such as those representing rollNumber, Name, etc. Create a class Exam by inheriting Student class.
# The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its
# own fields such as total_marks. Write an interactive program to model this relationship.
# ----------------------------------------------------------------------------------------------------------------------------

# Creating a 'student' class
class student:
    Name = ''
    rollno = 0

    # function to initialize the 'id' and 'name'
    def details(self, roll, name):
        self.Name = name
        self.rollno = roll


# Creating 'exam' class from 'student' class
class exam(student):
    marks = []

    # function to set the marks of that student
    def marks(self, marks):
        self.marks = marks
        return marks


# Creating 'result' class from 'exam' class.
class result(exam):
    # function to obtain the total marks of a student
    def student_result(self, marks_gain):
        total_marks = 0

        for mark in marks_gain:
            total_marks += mark

        return total_marks


# creating an object of the 'result' class
robj = result()

# asking the user to enter his/her name and roll no
student_name = input("Enter name of the student : ")
student_roll = input("Enter roll no. of the student : ")

# setting up the student details
robj.details(student_roll, student_name)

# asking the user to enter his marks for 6 subjects
print(f"Enter the marks of {student_name} in 6 subject : ")
marks = []

# reading the marks of student in 5 subjects and storing them
for i in range(6):
    marks.append(int(input()))

# setting up the student marks
marks_obtain = robj.marks(marks)

total = robj.student_result(marks_obtain)
print(f"Total marks of {student_name} is : {total}")
