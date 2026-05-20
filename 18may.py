'''#check the give number is even or odd
num=int(input("Enter a number:"))
if num%2==0:
    print("Number is Even")
else:
    print("Number is odd")'''
'''#check the give number is positive,negative and zero
num=int(input("Enter a number:"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print("number is zero")'''
'''#check number is divisible by 3&7 or not
num=int(input("Enter a number:"))
if num%3==0 and num%7==0:
    print("Number is divisible by 3 & 7.")
else:
    print("Number is not divisible by 3 & 7") '''
'''#find profit and loss using cost price and selling price
cost=int(input("Enter cost price:"))
selling=int(input("Enter selling price:"))
if selling>cost:
    profit=selling-cost
    print("profit is:",profit)
else:
    loss=cost-selling
    print("loss is:",loss)'''
'''#check the given number is leap year or not
year=int(input("Enter a year:"))
if year%4==0:
    print("leap year")
else:
    print("not a leap year")'''
'''#swap two numbers using third variable
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("After swapping:")
print("num1:",num1)
print("num2:",num2)'''
'''#find the maximum of three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>num2 and num>num3:
    print("num1 is maximum")
elif num2>num1 and num2>num3:
    print("num2 is maximum")
elif num3>num1 and num3>num2:
    print("num3 is maximum")
else:
    print("all numbers are equal")'''
'''#find the minimum of three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1<num2 and num1<num3:
    print("num1 is minimum")
elif num2<num1 and num2<num3:
    print("num2 is minimum")
elif num3<num1 and num3<num2:
    print("num3 is minimum")
else:
    print("all numbers are equal")'''
'''#print th sum of maximum and minimum number of three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
max_num=max(num1,num2,num3)
min_num=min(num1,num2,num3)
sum=max_num+min_num
print("maximum number is:",max_num)
print("minimum number is:",min_num)
print("sum of maximum and minimum numbers is:",sum)'''
'''#aceept 5 subject marks and print the total and percentage
sub1=int(input("Enter marks of subject 1:"))
sub2=int(input("Enter marks of subject 2:"))
sub3=int(input("Enter marks of subject 3:"))
sub4=int(input("Enter marks of subject 4:"))
sub5=int(input("Enter marks of subject 5:"))
total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
print("Total marks:",total)
print("Percentage:",percentage)'''