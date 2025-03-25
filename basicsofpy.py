#Pratice Questions

#Create variables to store your name, age, and favorite color. 
name = "naunehal khatri"
age = 20
fav_color = "black"
print(name)
print(age)
print (fav_color)


#Assign integer and floating-point values to two different variables and print them.
a = 2
b = 7.9
print (a)
print (b)

#Swap two variables without using a third variable.
myName = "naunehal"
surname = "khatri"
myName , surname = surname , myName
print(myName)
print(surname)


#Create a variable to store the value of Pi (3.14159) and print it
pi = 3.14159
print (pi)


#Assign a boolean value to a variable and print its type using type().
is_boolean = True
print(type(is_boolean))


#Type conversion Needs to be added in notes!
num1 = "20"
num2 = 12
result = int(num1) + num2
print(result)


#Create an expression that multiplies two numbers and stores the result in a variable.
a = 3
b = 5
result = a * b 
print (result)


#Combine a string variable with another string using concatenation.
name = "naunehal"
surname = "khatri"
Fullname = name + " " + surname
print (Fullname)


#Use an expression to calculate the area of a rectangle (length * width).
length = 2
width = 4
area = length * width
print("The area of a rectangle is:" , area)


#Evaluate the expression (10 + 5) * 2 - 3 and print the result.
result = (10 + 5) * 2 - 3
print ("The result of the expression is :" , result)


#Write an expression that converts temperature from Celsius to Fahrenheit using the formula F = C * 9/5 + 32.
C = 90
F = C * 9/5 + 32
print ("The temperature in Fahrenheit is :" , F)


#Compute the sum, difference, and product of two numbers.
a = 2
b = 4
print("The sum of the varibles is" , a + b)
print("The difference of the varibles is" , a - b)
print("The product of the varibles is" , a * b)


#Perform floor division between 25 and 4, then print the result.
a = 25
b = 4
division = a / b
print("The result of the division is :" , division )


#Compute the remainder when 50 is divided by 7.
a = 50
b = 7
reminder = a % b
print("The result of the reminder is :" , reminder )


#Use exponentiation to calculate 2^5.
a = 2
b = 5
exponentiation = a ^ b
print("The result of the exponentiation is :" , exponentiation )


#Write an expression that calculates the average of three numbers.
a = 2
b = 4 
c = 6
sum = a+b+C
avg = sum/3
print("The average of the three numbers is : " , avg)


#Compare two numbers using == and != and print the results.
a = 3
b = 3
result_equal = a == b
print("Are the numbers equal?" , result_equal)

result_not_equal = a != b
print("Are the numbers not equal?" , result_not_equal)


#Check if a number is greater than 100.
num = 120
result = num > 100
print("Is the number greater than 100? " , result)


#Compare the length of two strings.
str1 = "naunehal"
str2 = "khatri"
result = len(str1) > len(str2)
print("Is the first string longer than the second?" , result)


#Use >= to check if a person is eligible to vote (age >= 18).
ali = 24
can_vote = age >= 18
print("Can ali is eligible for vote:", can_vote)


#Compare the values of three different variables using > and <.
var1 = 10
var2 = 20
var3 = 30
result1 = var1 < var2 and var2 < var3 
result2 = var1 > var2 and var2 > var3 
result3 = var1 == var2 and var2 == var3 

print("Is var1 < var2 < var3?" , result1)
print("Is var1 > var2 > var3?" , result2)
print("Are var1 , var2 and var3 equal?" , result3)
