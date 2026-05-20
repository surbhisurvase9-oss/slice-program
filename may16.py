'''#write a python to check whether the given string is palindrome or not?
num=int(input("enter a number:"))
sr=int(num**0.5)
num1=sr*sr
if num1==num:
    print("yes")
else:
    print("No")'''
'''#write a python program that accept valid 10 digit number is it valid or not
mobile_no = eval(input("mobile no:"))
if isinstance(mobile_no,int) and len(str(mobile_no))==10:
    print("valid")
else:
    print("invalid")'''
'''#list number is valid or not
mobile_number = [9866743216, 9876543216, 9876543216,'9836543216',99765433332,'987,6543216']
for mob in mobile_number:
    if isinstance(mob,int) and len(str(mob))==10:
        print(mob)'''
'''#writw a program to print square of any number
num = int(input("enter a number:"))
print(num**2)'''

'''numbers=[1,2,3,5,7,9]
#write a program to print squaare of each number
#for loop is used to iterate over a sequence
for num in numbers:
    print(f"square of {num} is {num**2}")'''
    
'''numbers={1,2,3,5,7,9}
#create a dictionary to be present square of each number
square={}
for num in numbers:
    sq=num**2
    square[num] = sq
print(square)'''
'''#write a program to calcuaate the percentage of marks 
marks=int(input("enter marks:"))
total_marks=int(input("enter total marks:"))
percentage=(marks/total_marks)*100
print(percentage)'''
'''#write a calculate saling price
product_price=int(input("enter product price:"))
discount=int(input("enter discount percentage:"))
dp = (product_price*discount)/100
sp = product_price - dp
print(sp)''' 
'''#write a program to cal new_sal  after increment
salary=float(input("Enter the basic salary:"))
increment=float(input("Enter increment percentageP:"))
increment_amount=salary*increment/100
increment_salary=salary+increment_amount
print(increment_salary)'''
'''#write a program to calculate simple interest
p=float(input("Enter the principle amount:"))
r=float(input("Enter the interest rate:"))
t=int(input("Enter the time period:"))
si=p*r*t/100
print(si)'''
'''#write a program to calculate compund interest
p=eval(input("Enter the principle amount:"))
r=eval(input("Enter the interest rate:"))
t=eval(input("Enter the time period:"))
interest=p*(1+r/100)**t
ci=interest-p
print(interest)
print(ci)'''
'''#write a program to calculate length of diagonal
l=float(input("Enter the length:"))
b=float(input("Enter the breadth:"))
diagonal=((l**2)+(b**2))**0.5
print(diagonal)'''
'''#write a program to convert meter centemeter
meter=eval(input("Enter value in meters:"))
centemeter=meter*100
print(0centemeter)'''
#