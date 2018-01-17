# numInInches = 5
# conversionInchesToCentimeters = 2.54
# numInCentimeters = numInInches * conversionInchesToCentimeters
# print("%s inches = %s centimeters" %(numInInches,numInCentimeters))


# ##From Inch to Feet
# numInInches = 12
# conversionFeetToInches = 12
# numInFeet = numInInches / conversionFeetToInches
# print("%s inches = %s feet" %(numInInches, numInFeet))

##Celsius to Farenheit

# celsius = 100
# celsiusToFahrenheit = celsius * 9.0 / 5.0 + 32
# print("%s Celsius is = %s Farenheit" % (celsius, celsiusToFahrenheit))

# # List
# x = [1,7,21,3,23]
# x.append(5)
# del x[2]
# print(x)

# # map
# z = {"zaa":5, "g":35, "n":35}
# z["n"] = 36
# z["g"] = 34
# z["zaa"] = 4

# # tuple
# y = (3,74,27,3,4)
# print(y[0]+y[4])


# if then else
#
# age = 40
# if age == 10:
#     print("What do you call an unhappy cranberry?")
#     print("A blueberry!")
# elif age == 11:
#     print("What did the green grape say to the blue grape?")
#     print("Breathe! Breathe!")
# elif age == 12:
#     print("What did 0 say to 8?")
#     print("Hi guys!")
# elif age == 13:
#     print("Why wasn't 10 afraid of 7?")
#     print("Because rather than eating 9, 7 8 pi.")
# else:
#     print("Huh?")

## temperature = -6
#
# if temperature >= 20:
#     print("Its pudut")
# elif temperature < 0:
#     print("freeezing!")
# else:
#     print("Lamin")

# odd/even
# number = 8
#
# if number % 2 == 0:
#     if number <= 10:
#         print("Hello")
#     else:
#         print("World")
# else:
#     print("Number is odd")


# aList = [1,7,21,3,23]
#
# for x in aList:
#     print("Hello")
#     print("%s" % (x))
#     print()
#
# for x in range (-5,0):
#     print("ZZZ")

##
# for x in range (1,11):
#     y = x * 10
#     print("%s" % (y))


# for x in range (1,11):
#     print("%s" % (x*2))

# for x in range (1,11):
#     print("%s" % (x*2-1))

# y = 0
# for x in range (1,11):
#     print("%s" % (x + y))
#     y = x

# listA = [1,5,8,90,4,2,1]
# for x in listA:
#     if x % 2 == 0:
#         print("%s is even" % (x))
#         print("Hello World")
#         print()
#     else:
#         print("%s is odd" % (x))
#         print()
#
# x = 2
# while x <= 15:
#     print("Hello World")
#     x = x + 3
#
# for x in range(0, 20):
#     print('hello %s' % x)
#     if x < 9:
#         break

# x = 1
# while x<= 35:
#     print()

# age = 36
#
# if age % 2 == 0:
#     number = 2
# else:
#     number = 1
#
# while number <= age:
#     print("%s" %(number))
#     number = number + 2


# ingredients = ['snails', 'leeches', 'gorilla belly-button lint','caterpillar eyebrows', 'centipede toes']
#
# num = 1
# for item in ingredients:
#     print("%s %s" % (num,item))
#     num = num + 1

# earthWeight = 74
# for year in range(1,16):
#     moonWeight = earthWeight * 0.165
#     print("Year %s - Earth weight = %s; Moon Weight = %s" % (year,earthWeight,moonWeight))
#     earthWeight = earthWeight + 1

# earthWeight = 74
# year = 1
# while year <= 15:
#     moonWeight = earthWeight * 0.165
#     print("Year %s - Earth weight = %s; Moon Weight = %s" % (year,earthWeight,moonWeight))
#     earthWeight = earthWeight +
#     year = year + 1

#1: Favorite things(Page 41):
# games = ["badminton", "swimming", "basketball","netball"]
# foods = ["chocolate", "olives", "cheeze"]
# favorites = games + foods
# print(favorites)

#2: Counting Combatant(Page 42):
# ninjasAndSamurai = (3*25) + (2*40)
# print(ninjasAndSamurai)

#3: Greetings!
# firstName = ("Natalie")
# lastName = ("Batara")
# print("Hi there, %s %s" % (firstName,lastName))

#2: Twinkies (Page 65)
# twinkies = 501
# if twinkies < 100 or twinkies > 500:
#     print("Too few or too many")

# # Money
# money = 501
# if (money > 100 and money < 500) or (money > 1000 and money < 5000):
#     print("true")

#4: I Can Fight Those Ninjas
# Create an if statement that prints the string “That’s too many”
# if the variable ninjas contains a number that’s less than 50, prints
# “It’ll be a struggle, but I can take ’em” if it’s less than 30, and
# prints “I can fight those ninjas!” if it’s less than 10.

# if ninjas < 10:
#     ninjas = 28
#     print("I can fight those ninjas!")
# elif ninjas < 30:
#     print("It\'ll be a struggle, but I can take /'em")
# elif ninjas <50:
#     print("That\'s to many")

# for x in range(0, 20):
#     print('hello %s' % x)
#     if x < 9:
#         break

## Project TASK LIST
# print ("Please choose from the list below:")
# print ("Choose from the list below: ")

# items = []
# i=0
# while 1:
#     i+=1
#     item = input("Enter item %d: " %i)
#     if item == "":
#         break
#     items.append(item)
#     print(items)
# print("Thats your list: ")
# print(items)


