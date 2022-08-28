 # Create class "Student"

class Student:
 

  # Constructor

    def __init__(self, name, rollno, m1, m2):

        self.name = name

        self.rollno = rollno

        self.m1 = m1

        self.m2 = m2
 

    # Function to create and append new student

    def accept(self, Name, Rollno, marks1, marks2):

   

  # use ' int(input()) ' method to take input from user

        ob = Student(Name, Rollno, marks1, marks2)

        ls.append(ob)
 

    # Function to display student details

    def display(self, ob):

        print("Name : ", ob.name)

        print("RollNo : ", ob.rollno)

        print("Marks1 : ", ob.m1)

        print("Marks2 : ", ob.m2)

        print("\n")
 

    # Search Function

    def search(self, rn):

        for i in range(ls.__len__()):

            if(ls[i].rollno == rn):

                return i
 

    # Delete Function

    def delete(self, rn):

        i = obj.search(rn)

        del ls[i]
 

    # Update Function

    def update(self, rn, No):

        i = obj.search(rn)

        roll = No

        ls[i].rollno = roll
 
 
# Create a list to add Students

ls = []
# an object of Student class

obj = Student('', 0, 0, 0)
 

print("\nOperations used, ")

print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
 
# ch = int(input("Enter choice:"))
# if(ch == 1):

obj.accept("shirisha", 1, 100, 100)

obj.accept("saritha", 2, 90, 90)

obj.accept("Jyothi", 3, 80, 80)
 
# elif(ch == 2):

print("\n")

print("\nList of Students\n")

for i in range(ls.__len__()):

    obj.display(ls[i])
 
# elif(ch == 3):

print("\n Student Found, ")

s = obj.search(2)
obj.display(ls[s])
 
# elif(ch == 4):

obj.delete(2)

print(ls.__len__())

print("List after deletion")

for i in range(ls.__len__()):

    obj.display(ls[i])
 
# elif(ch == 5):

obj.update(3, 2)

print(ls.__len__())

print("List after updation")

for i in range(ls.__len__()):

    obj.display(ls[i])
 
# else:

print("Thank You !")

Output:
Operations used,

1.Accept Student details
2.Display Student Details
3.Search Details of a Student
4.Delete Details of Student
5.Update Student Details
6.Exit



List of Students

Name   :  shirisha
RollNo :  1
Marks1 :  100
Marks2 :  100


Name   :  saritha
RollNo :  2
Marks1 :  90
Marks2 :  90


Name   :  Jyothi
RollNo :  3
Marks1 :  80
Marks2 :  80



 Student Found,
Name   :  saritha
RollNo :  2
Marks1 :  90
Marks2 :  90


2
List after deletion
Name   :  shirisha
RollNo :  1
Marks1 :  100
Marks2 :  100


Name   :  Jyothi
RollNo :  3
Marks1 :  80
Marks2 :  80


2
List after updation
Name   :  shirisha
RollNo :  1
Marks1 :  100
Marks2 :  100


Name   :  Jyothi
RollNo :  2
Marks1 :  80
Marks2 :  80


Thank You !
