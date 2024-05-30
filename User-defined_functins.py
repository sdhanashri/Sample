# def Addition():
#     a=int(input("Enter the 1st number: "))
#     b=int(input("Enter the 2nd number: "))
#     print(a+b)

# Addition()

# def Addition(a,b):
#     print("Addition is: ",a+b)

# Addition(10,20)

#**************  NON-PARAMETERIZED FUNCTIONS  ***************

# def func():
#     tech1="python"
#     tech2="Django"
#     print("This is {} and {} training.".format(tech1,tech2))

# func()

#**************  PARAMETERIZED FUNCTIONS  ******************

# def func(tech1,tech2):
#     print("This is {} and {} training!".format(tech1,tech2))

# func("python","Django")


#1)Positional

# def student(name,age):
#     print("Name is: ",name)
#     print("Age is: ",age)

# student("Dhanashri",22)

# #2)Keyword

# def student(name,age):
#     print("Name is: ",name)
#     print("Age is: ",age)

# student(age=22, name="Dhanashri")

# #3)Default

# def student(name,age=20):
#     print("Name is: ",name)
#     print("Age is: ",age)

# student(age=25,name="abc")

# #4)Variable Length/non keyword variable length

# def student(name,age,*args):
#       print(name,age)
#       for i in args:
#           print(i)

# student("abc",23,448,869,890,900)

# #5)Keyword variable length    

# def info(**kwargs):
#     for k,v in kwargs.items():
#         print("name is:",k, "value is: ",v)

# info(name="varsha",mname="rahul",lname="rajguru")

# def student(name,age,**kwargs):
#       print(name,age)
#       for k,v in kwargs.items():
#           print(k,v)

# student(name="abc",age=23,mango=448,apple=869,orange=890,cherry=900)


#******************************TASK************************************

#1)Write a program to create a function show_employee() using the following conditions.
    # It should accept the employee’s name and salary and display both.
    # If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name,salary=9000):
#     print("Employee name: ",name)
#     print("Salary: ",salary)

# show_employee("Dhanashri",salary=20000)

# #2)Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

# def display_student(name="sakshi",age=20):
#     print("Name: ",name)
#     print("Age: ",age)


# display_student(name="Dhanashri")
# show_student=display_student
# show_student(name="rahul")

# #3)Return multiple values from a function.  return both addition and subtraction in a single return call.

# def arith_ope(a,b):
#     print("Addition is: ",a+b)
#     print("Substraction is: ",a-b)

# arith_ope(40,10)

# a=int(input("Enter the 1st number: "))      #Take input from user
# b=int(input("Enter the 2nd number: "))
# def arithmatic(a,b):
#     print("Addition is: ",a+b)
#     print("Substraction is: ",a-b)

# arithmatic(a,b)

# #4)Write a program to create function func1() to accept a variable length of arguments and print their value.
    
# def func1(name,div,*args):
#     print("Name: ",name)
#     print("Div: ",div)
#     for i in args:
#         print(i)

# func1("Dhanashri","A",23,45,36,49)

# #4)Using keyword variable length

# def func2(name,div,**kwargs):
#     print("Name: ",name)
#     print("Div: ",div)
#     for k,v in kwargs.items():
#         print(k,v)

# func2("Dhanashri","A",age = 20,Technology="Data Analytics")

# 5)Python Program to find the area of triangle using function .take input from user .first side, second side, third side

# b=int(input("Enter the base of triangle: "))
# h=int(input("Enter the height of triangle: "))
# def area_of_triangle(base,height):
#     print("Area of Triangle: ",(1/2)*base*height)

# area_of_triangle(b,h)

# 6)Find the largest item from a given list  x = [4, 6, 8, 24, 12, 2]
    
# x=[4,6,8,24,12,2]

# print("The largest item from given list is: ",max(x))

# 7)Write a program that subtracts two numbers using function

# def subtraction():
#     a=int(input("Enter the 1st num: "))
#     b=int(input("Enter the 2nd num: "))
#     print("substraction is: ",a-b)
# subtraction()

# 8)Write a program to swap two numbers

# def swap(a,b):                      #using function
#     a,b=b,a
#     return a,b

# a=int(input("Enter 1st num: "))
# b=int(input("Enter 2nd num: "))
# print(swap(a,b))

#         #OR

# x = 5                               #without using function , without using third variable
# y = 7
# print ("Before swapping: ")
# print("Value of x : ", x, " and y : ", y)
 
# x, y = y, x

# print ("After swapping: ")
# print("Value of x : ", x, " and y : ", y)

        #OR

# x = 5                                   #swapping using third variable
# y = 10

# temp = x
# x = y
# y = temp

# print('The value of x after swapping: {}'.format(x))
# print('The value of y after swapping: {}'.format(y))


# 9)Write a program to return the average of its arguments.

# def average(a,b):
#     c=a+b/2
#     return c
# print(average(10,15))

# 10)Write a program using functions and return statement to check whether a number is even or odd.

# def evenodd():
#     a=int(input("Enter the number: "))
#     if (a%2==0):
#         print("Number is Even")
#     else:
#         print("Number is odd")

# evenodd()

# 11)write a program to calculate simple interest. Suppose the customer is senior citizen. 
    #He is being offered 12 per cent rate of interest; for all the customers, the ROI is 10 per cent.

# def simple_interest(a,p,t):
#     print("Age of person: ",a)
#     print("Principal is: ",p)
#     print("Time period is: ",t)

#     if a>=60:
#         si=(p*t*12)/100
#         print("Simple interest is: ",si)
#     else:
#         SI=(p*t*10)/100
#         print("Simple interest is: ",SI)

# a=int(input("Enter the age of person: "))
# p=int(input("Enter the principal amount: "))
# t=int(input("Enter the time period: "))

# simple_interest(a,p,t)

# 12)To write a function that displays a string repeatedly

# def repeat_string(word,n,dhanashri):
#     x=word*n
#     return x
# print(repeat_string('\nDhanashri',4,'dhanashri'))
#                     #OR
# str = '\nSonawane'                                  #without function
# print(str*3)
                    #OR
# def repeat(word,n):
#     print(word*n)
# def main():
#     string=input("Enter the string: ",)
#     n=int(input("Insert no. of  repitation: "))

#     repeat(string,n)
# main()

# 13)Write a program to convert time into minutes

# def convert_time(hrs,min):
#     min=hrs*60+min
#     return min
# h=int(input("Enter the hours: "))
# m=int(input("Enter the minutes: "))
# m=convert_time(h,m)
# print("Total minutes: ",m)

# 14)Write a program to return the full name of a person

# def name(name,mid_name,last_name):
#     print(name,mid_name,last_name)

# name('Dhanashri','Sharad','Sonawane')
            #OR
# def name(name,mid_name,last_name):
#     print(name,mid_name,last_name)

# a=input("Enter the name: ")
# b=input("Enter the middle name: ")
# c=input("Enter the last name: ")

# name("Full name is: ",name=a,mid_name=b,last_name=c)

# 15)Write a program that greets a person

# def greet(name):
#     print("Hello",name)

# name=input("Enter the name: ")
# greet(name)

            #OR

# import random
# def greet(greeting, name):
#     print(greeting,name)

# name=input("Enter the name: ")
# choices=['Hii','Hello','Good morning']
# greeting=random.choice(choices)

# greet(greeting,name)
    
# 16)Write a program to print the Fibonacci series using recursion

# Python program to display the Fibonacci sequence

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = int(input("Enter the no. of terms: "))

# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))




# n = 10                              #without using function
# num1 = 0
# num2 = 1
# next_number = num2  
# count = 1
 
# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# print()


# 17)Write a program to generate 10 random numbers between 1 to 100

# import random
 
# num = 10
# start = 1
# end = 100
 
# result = random.sample(range(start, end + 1), num)
 
# print(result)


#18)Write a program to display the date and time using the time module

# import datetime as dt

# now=dt.datetime.now()           
# print(now)

#19)Write a program that prints the calendar of a particular month

# import calendar
# print(calendar.month(23,12))

#********************************TASK- 1)CALCULATOR*****************************

# def Addition():
#     print("Addion of given number is : ",x+y)

# def Substraction():
#     print("Substraction of given number is : ",x-y)

# def Multiplication():
#     print("Product of given number is : ",x*y)

# def Division():
#     print("Division of given number is : ",x/y)

# print("  CALCULATOR  ")
# print("\n1. Addition")
# print("\n2. Substraction")
# print("\n3. Multiplicaton")
# print("\n4. Division")

# count=0
# while count<=4:
#     count+=1

#     choice = int(input("\nEnter the Choice(1/2/3/4): "))

#     x=int(input("Enter the 1st number: "))
#     y=int(input("Enter the 2nd number: "))

#     if choice == 1:
#         Addition() 
        
#     elif choice == 2:
#         Substraction()

#     elif choice == 3:
#         Multiplication()

#     elif choice == 4:
#         Division()

#     else:
#         print("Please enter the valid choice.")

#TASK - 2)RAILWAY RESERVATION SYSTEM

# def train_details(total_seats,reserved_seats):
#     print("Total seats: ",total_seats)
#     print("Reserved seats: ",reserved_seats)

# def reservation(name,seat_no,no_of_seats):
#     print("\nEnter the name: ",name)
#     print("Enter the seat no.: ",seat_no)
#     print("Enter the no. of seats: ",no_of_seats)

# train_details(100,75)
# reservation("Dhanashri","76,77,78",3)


# a=input("\nEnter the name: ")                         #take input from user
# b=input("Enter the seat no.: ")
# c=input("Enter the no. of seats: ")
# def reservation(a,b,c):
#     print("Name: ",a)
#     print("Seat no.: ",b)
#     print("No.of seats: ",c)

# def train_details(total_seats,reserved_seats):
#     print("\nTotal seats: ",total_seats)
#     print("Reserved seats: ",reserved_seats)

# train_details(100,75)
# reservation(a,b,c)


# count=1                                             #Using if-elif-else and functions
# while count<=3:
#     count+=1

#     def train_details(total_seats,reserved_seats):
#         print("Total seats: ",total_seats)
#         print("Reserved seats: ",reserved_seats)


#     def reservation(name,seat_no,no_of_seats):
#         # name=input("\nEnter the name: ")
#         # seat_no=input("Enter the seat no.: ")
#         # no_of_seats=input("Enter the no. of seats: ")
#         print("\nEnter the name: ",name)
#         print("Enter the seat no.: ",seat_no)
#         print("Enter the no. of seats: ",no_of_seats)

#     def exit():
#         print("Thank You...!!!")

#     print("RAILWAY RESERVATION SYSTEM")
#     print("\n1. Train Details")
#     print("2. Reservation")
#     print("3. Exit")

#     ch= int(input("Enter the choice(1/2/3): "))

#     if ch==1:
#         train_details(100,75)

#     elif ch==2:
#         reservation("Dhanashri","76,77,78",3)

#     elif ch==3:
#         exit()

#     else:
#         print("Please enter the valid choice.")
