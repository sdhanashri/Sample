# 1) Pallindrome Number Program
     # A palindrome number is a number that reads the same forward and backward.

# def is_palindrome(string):
#     reversed_string = string[::-1]
#     return string == reversed_string

# word = input("Enter the String: ")
# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")

            # OR
    
num = input("Enter a number: ")
if num == num[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome") 

# 2) Armstrong Number Program
#    If the sum of the nth power of each digit equals to the number itself.

# n = int(input("Enter any number: "))  
# o = n  
# l = len(str(n))
# sum1 = 0

# while n != 0:
#     r = n % 10
#     sum1 = sum1+(r**l)
#     n = n//10

# if o == sum1:
#     print("The given number", o, "is armstrong number")
# else:
#     print("The given number", o, "is not armstrong number")

# 3) Fibonacci Series Program
    
# n = 10
# num1 = 0
# num2 = 1
# next_number = num2 
# count = 1

# while count <= n:
# 	print(next_number)
# 	count += 1
# 	num1, num2 = num2, next_number
# 	next_number = num1 + num2
# print()

# 4) Reverse Program 

# n = int(input("Enter the Number: "))
# print(str(n)[::-1])

# 5) Prime Number Program

# num = int(input("Enter the number: "))

# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# 6) Factorial Number Program

# n=int(input("Enter the number: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("The factorial of given num is: ",fact)

# 7)Print all even and odd numbers in range 1 to 100

# for i in range(1,100,2):
#     print(i)            #odd number
   
# for j in range(2,101,2):
#     print(j)            #even number


