theater = "XYZ"
ageLimit = 18

print("welcome to the {} theaters".format(theater))

userInput = input("enter your age here:")
print("user input is {}".format(userInput))

# if int(userInput) >= ageLimit:
#     print("okay, your age is {} you are eligible".format(userInput))
# else:
#     adultPresent = input("is another adult with you? : yes or no")
#     if adultPresent == 'yes':
#     print("enjoy the movie")
# else:
#     print("your age is you are not eligible")

if int(userInput) >= ageLimit:
    print("Okay, your age is {}. You are eligible.".format(userInput))
else:
    adultPresent = input("Is another adult with you? (yes or no): ")
    if adultPresent.lower() == 'yes':
        print("Enjoy the movie!")
    else:
        print("Your age is {}, you are not eligible.".format(userInput))


