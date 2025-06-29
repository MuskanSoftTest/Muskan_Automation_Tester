# Write a program to assign grades based on marks
# If marks >= 90 ➔ Grade A
# Else if marks >= 80 ➔ Grade B
# Else if marks >= 70 ➔ Grade C
# Else ➔ Fail

studName = str(input("Please enter your name: "))
studMarks =  int(input("enter marks here"))

if studMarks >= 90:
    print("{} your grade is A".format(studName))
elif studMarks >= 80:
    print("{} your grade is B".format(studName))
elif studMarks > 70:
    print("{} your grade is C".format(studName))
else:
    print("{} you are Fail".format(studName))