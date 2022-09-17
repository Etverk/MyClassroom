#Imports
import math
import re
import random

#Input
# Jonathan W, Eric J, Henrik K, John A, Marcus B, Liam M, Olivia C, Noah K, Emma S, Charlotte Z, Amelia F, Lucas H, Theodore L, James R, David K, William S, Elizabeth E, Susan J, Thomas H, Charles K, Karen W, Daniel G, Betty J, Alexander P, Raymond C, Helen S, Christine J, Catherine Z, Nicholas A, Emma F, Jordan A, Bryan H
studentListInput = "Jonathan W, Eric J, Henrik K, John A, Marcus B, Liam M, Olivia C, Noah K, Emma S, Charlotte Z, Amelia F, Lucas H, Theodore L, James R, David K, William S, Elizabeth E, Susan J, Thomas H, Charles K, Karen W, Daniel G, Betty J, Alexander P, Raymond C, Helen S, Christine J, Catherine Z, Nicholas A, Emma F, Jordan A, Bryan H"
#studentListInput = input("Please enter all students' names, separated by a comma and a space.")
studentList = studentListInput.split(", ")
print(len(studentList))
for i in studentList:
    print(i)

#Randomise list of students
randomStudentList = random.sample(studentList, len(studentList))
print(randomStudentList)