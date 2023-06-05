#lAB1 - INPUT FUNCTION
name = input("Enter Your Name To Start The Game: ")
level = input("Enter Your Level Number To Continue The Game: ")
print("Hello " + name + " You Are At Level "  + level + "")

name = input("Enter Your Name To Start The Game: ")
Preference = input("Do you like Japan or South Korea? ")
print("Hello " + name + "." "  You said that you like " + Preference + ","  " You are a verified Traveller!")

name = input("What is your name? ")
age = input("How old are you? ")
feeling = input("How do you feel, good or great? ")
print("Hello " + name + "." " You are " + age + " years old" " and you feel " + feeling + "."   " Keep shining Bro!")

#LAB 2 - BUILDING A CALCULATOR USING THE INPUT FUNCTION
number1 = input("Please enter a number: ")
number2 = input("Please enter a second number: ")
result = int(number1) + int(number2)
print(result)

number1 = input("Please enter a number: ")
number2 = input("Please enter a number: ")
result = int(number1) * int(number2)
print(result)

number1 = input("Please enter a number: ")
number2 = input("Please enter a number: ")
number3 = input("Please enter a number: ")
result = int(number1) * int(number2) - int(number3)
print(result)

number1 = input("Please enter a number: ")
number2 = input("Please enter a second number: ")
result = float(number1) + float(number2)
#print(result)

number1 = input("Please enter a number: ")
number2 = input("Please enter a number: ")
number3 = input("Please enter a number: ")
result = float(number1) * float(number2) - float(number3)
print(result)

#LAB 3 - BUILDING A PROMPT REPLY FROM A USER
print("Hi user, how would you rate your mood on a scale from 1 to 10")

mood_rating = input()
print("You feel like a " + mood_rating + "." " Thanks for letting us know!")

print("Hi user, how bad do you want to travel and leave the UK on a scale from 1-10? ")

travel_rating = input()
print("The level that you want to leave the UK is a " + travel_rating + "." "I hope you get out ASAP!")
