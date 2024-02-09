print("Welcome to my Computer Quiz Game")
print("This is a Quiz Game Project Created By Varad Sandeep Naik Using Python3")
print("Hope You Enjoy The Game :)")

start = input("Should We Start The Game? ").lower()

if start != "yes":
    quit()

score = 0

print("Great ! Let's Go Ahead")

answer = input("Question 1) What Does PSU Stand for in Computers?\n Answer ---> ").lower()
if answer == "power supply unit":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 2) In a computer, most processing takes place in _______?\n Answer ---> ").lower()
if answer == "cpu" or answer == "central processing unit":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 3) EEPROM stands for _______?\n Answer ---> ").lower()
if answer == "electronic erasable programmable read only memory":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 4) The first web browser is _______?\n Answer ---> ").lower()
if answer == "mosaic":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 5) IBM stands for _______?\n Answer ---> ").lower()
if answer == "international business machines":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 6) First page of Website is termed as _______?\n Answer ---> ").lower()
if answer == "homepage":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 7) No. of different characters in ASCII coding system?\n Answer ---> ").lower()
if answer == "1024":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 8) A fault in a computer program which prevents it from working correctly is known as _______?\n Answer ---> ").lower()
if answer == "bug":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 9) Which button makes alphabets/letters in uppercase and lowercase and numbers to symbols?\n Answer ---> ").lower()
if answer == "shift":
    print("     Correct ! Let's Continue with next Question")
    score += 1
else:
    print("     Incorrect Answer ! Dont Worry You will get the next one Correct :)")

answer = input("Question 10) Which command is used to select the whole document?\n Answer ---> ").lower()
if answer == "ctrl+a":
    print("     Correct ! You are Done With The Quiz")
    score += 1
else:
    print("     Incorrect Answer ! Let's See your score :)")

print("Great Game ! So Your Score is " + str(score) + " out of 10")
print("Your Percentage is " + str((score / 10)*100) + "%")

