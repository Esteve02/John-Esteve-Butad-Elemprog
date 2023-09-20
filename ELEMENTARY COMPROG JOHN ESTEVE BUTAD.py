#promt the user to enter the student name, id#, course and section

name = input(" enter student name ")
idnum = input("enter a student id ")
course_sec = input(" enter course and section ")

# assign of value of grades
grade1 = eval(input('1st quarter grade: '))
grade2 = eval(input('2nd quarter grade: '))
grade3 = eval(input('3rd quarter grade: '))
grade4 = eval(input(' 4th quarter grade: '))

#assign value of grades for ave.

numofgrades = 4

# compute of ave.

ave = grade1 + grade2 + grade3 + grade4 / numofgrades
print('student name:', name)
print('ID number:', idnum)
print(' course and section:' , course_sec)
print('Your Average of Grades is' , ave)

