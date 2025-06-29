a=10
b=12
c=4
d=7

# Example 1
# if a>b:
#     print("a is greater than b")
# else:
#     print("a is less than b")

# Example 2
# if a>b:
#     print("a is greater than b")
# elif(c<d) and (b<d):
#     print("b is less than d")
# elif(d>b):
#     print("d is greater than b")
# else:
#     print("b is less than d")

subject = ["english", "marathi", "hindi", "maths"]
marks = [80, 45, 98, 37]

my_sub = "78"

if my_sub in subject:
    print("Yes, my subject is " + my_sub)
elif my_sub in marks:
    print("Yes, my marks is ")
elif my_sub not in subject:
    print("No, its a mark of subject")
else:
    print("unknown subject " + my_sub)