# # Simple task list program
#
# print("TASK LIST")
# print()
#
# items = []
#
# while True:
#     print("Choose option:")
#     print("1. Add an item to the list")
#     print("2. Remove an item in the list")
#     print("3. Display list")
#     print("4. Reset list")
#     print("5. Exit")
#     print()
#     option = int(input("Option:"))
#
#     if option == 1:
#         itemToAdd = input("Enter the value for item:")
#         items.append(itemToAdd)
#     elif option == 2:
#         itemPositionToRemove = int(input("Enter item position to remove:"))
#         del items[itemPositionToRemove]
#     elif option == 3:
#         print("List is: ")
#         print(items)
#     elif option == 4:
#         items = []
#     elif option == 5:
#         break
#     else:
#         print("Wrong option. Choose only from 1 to 5")
#     print()

# CASE 1:
# print("Hello, Natalie")

# CASE 2:
# num1 = 10
# num2 = 20
# sum =num1 + num2
# print(sum)

# # CASE 3:
# num1 = 20
# num2 = 10
# difference= num1 - num2
# print("The difference of %d and %d is %d" % (num1,num2,difference))

# # CASE 4:
# inch = int(input("Enter value for inch: "))
# inchToCm= inch * 2.54
# print("%d inch is equal to %d cm" % (inch, inchToCm))

# # CASE 5: Odd or Even
# x = int(input("Enter a number: "))
# if x % 2 ==0:
#     print("Number is %d is EVEN" % (x))
# else:
#     print("Number %d is ODD" % (x))

# CASE 6:
# number = int(input("Enter a number: "))
# if number % 2 != 0:
#     print("%d is Odd" % (number))
# elif number % 2 == 0 and number < 10:
#     print("%d is Even and less than 10" % (number))
# elif number %2 == 0 and number == 10:
#     print("%d is Even and equal to 10" % (number))
# else:
#     print("%d is Even and greater than 10" % (number))

# CASE 7 :
# grade = int(input("Enter a grade: "))
# if grade < 75:
#     print("Failed")
# elif grade >= 75 and grade < 80:
#     print("Average")
# elif grade >= 80 and grade < 90:
#     print("Very Good")
# elif grade >= 90 and grade <= 100:
#     print("Excellent")
# else:
#     print("Invalid input")

# CASE 8:

# for x in range(1,6):
#     print("Natalie %d " % (x))


# CASE 9:

# gender = input("Enter gender: ")
# age = int(input("Enter age: "))
#
# if gender == 'female' or gender == 'f' or gender == 'Female' or gender == 'F':
#     if age <= 25:
#         print("You are a Daughter")
#     elif age > 25 and age <= 60:
#         print("You are a Mother")
#     elif age > 60:
#         print("You are a Grandma")
# elif gender == 'male' or gender == 'm' or gender == 'Male' or gender == 'M':
#     if age <= 25:
#         print("You are a Son")
#     elif age > 25 and age <= 60:
#         print("You are a Father")
#     elif age > 60:
#         print("You are a Grandpa")
# else:
#     print("Invalid input")

# CASE 10:

# numInCentimeter = int(input("Enter centimeter value: "))
# print("Choose options: ")
# print()
# print("1. Convert to Inch")
# print("2. Covert to Millimeter")
# option = int(input("Option: "))
# print()
#
# if option == 1:
#     numToInch = numInCentimeter / 2.54
#     print("%s centimeter is %s inch" % (numInCentimeter, numToInch))
# elif option == 2:
#     numToMm = numInCentimeter * 100
#     print("%s centimeter is %s Millimeter" % (numInCentimeter, numToMm))
# else:
#     print("Invalid input")

