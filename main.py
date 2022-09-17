#Imports
import math
import re
import random
import numpy

# Input
# Jonathan W, Eric J, Henrik K, John A, Marcus B, Liam M, Olivia C, Noah K, Emma S, Charlotte Z, Amelia F, Lucas H, Theodore L, James R, David K, William S, Elizabeth E, Susan J, Thomas H, Charles K, Karen W, Daniel G, Betty J, Alexander P, Raymond C, Helen S, Christine J, Catherine Z, Nicholas A, Emma F, Jordan A, Bryan H
studentListInput = "Jonathan W, Eric J, Henrik K, John A, Marcus B, Liam M, Olivia C, Noah K, Emma S, Charlotte Z, Amelia F, Lucas H, Theodore L, James R, David K, William S, Elizabeth E, Susan J, Thomas H, Charles K, Karen W, Daniel G, Betty J, Alexander P, Raymond C, Helen S, Christine J, Catherine Z, Nicholas A, Emma F, Jordan A, Bryan H"
#studentListInput = input("Please enter all students' names, separated by a comma and a space.")
studentList = studentListInput.split(", ")
print(len(studentList))
for i in studentList:
    print(i)

# Randomise list of students
randomStudentList = random.sample(studentList, len(studentList))
print(randomStudentList)

# Classroom
classroomWidth = 5#input("Enter the width of the classroom.") # Width = num of values in list
classroomLength = 10#input("Enter the length of the classroom.") # Length = num of lists in matrix

classroomMatrix = []
for i in range(classroomLength):
    classroomMatrix.append([])
    print(i)

for i in classroomMatrix:
    for y in range(classroomWidth):
        i.append(None)

# Assign seatings
x = 0
for i in classroomMatrix:
    for y in range(classroomWidth):
        try:
            i[y] = randomStudentList[x]
            x += 1
        except IndexError:
            pass
        
        
print(numpy.matrix(classroomMatrix))
    
