theater = "XYZ"
ageLimit = 18

print("welcome to the {} theaters".format(theater))

userInput = input("enter your age here:")
print("user input is {}".format(userInput))

if int(userInput) >= ageLimit:
    print("okay, your age is {} you are eligible".format(userInput))
else:
    print("your age is {} you are not eligible".format(userInput))



