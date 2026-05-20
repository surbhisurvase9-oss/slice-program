#check user age for eligibility user age is above 18 and below 75 then he is eligible for applying rto license display apropreate msg to user as per age criteria for less age display wait for---years age is above 75 then display you are age bar other wise welcome to punr rto portal. input,data type casting.if,if -else,if-elif-else
"""age=int(input("Enter your age:"))
if(age>=18):
    print("welcome to pune RTO portal")
elif(age<75):
    print("welcome to pune RTO portal")
else:
    print("you are not eligible for Rto portal ")"""
    
age=int(input("Enter your age:"))
if(18<= age <75):
    print("you are eligible")
elif(age<18):
    print(f"wait for{18-age}years---")
else:
    print("Age bar")