"""#Accept student Information -student name,marks.percentage display rahul scored 450 marks with 90.0% percentage
Name = input("Enter Student Name:")
Marks = int(input("Enter thhe Student Marks:"))
Percentage = float(input("Enter the Student Percentage:"))
s=f"{Name} scored {Marks} marks with {Percentage}% percentage."
print(s)"""
"""#Accept age from user and display age after 10 years to user  "Your age after 10 year will be 30
a = int(input("Enter your age:"))#int converts input string to integer format,we can only add integer
age = a + 10
s = f"Your age after 10 year will be {age}."
print(s)"""
'''#create table
Name = "surbhi"
Name1 = "pranjal"
Name2 = "sejal"
Marks1 = '88'
Marks2= '90'
Marks3= '95'
print("-"*16)
print("| Name | Marks |")
print("-"*16)
print(f"|{Name:<0} |{Marks1:>5} |")
print("-"*16)
print(f"|{Name1:<1} |{Marks2:>5} |")
print("-"*16)
print(f"|{Name2:<1} |{Marks3:>5} |")
print("-"*16)'''
#create report card
Name = input("Enter student name:")
a1= input("Enter subject name:")
a2= input("Enter subject name:")
a3= input("Enter subject name:")
a4= input("Enter subject name:")
a5= input("Enter subject name:")
b1= int(input("Enter subject marks:"))
b2= int(input("Enter subject marks:"))
b3= int(input("Enter subject marks:"))
b4= int(input("Enter subject marks:"))
b5= int(input("Enter subject marks:"))
total_marks = b1 + b2 + b3 + b4 + b5
print("***** The Kiran Academy Report Card *****")
print("-"*39)
print(f" *** Student Name: {Name} ***")
print("-"*28)
print(" | Subject name | Marks|")
print("-"*23)
print(f"{a1}            {b1}")
print(f"{a2}            {b2}")
print(f"{a3}            {b3}")
print(f"{a4}            {b4}")
print(f"{a5}            {b5}")
print("-"*28)
print(f"Total Marks: {total_marks}")