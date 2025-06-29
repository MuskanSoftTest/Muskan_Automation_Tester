# >0 = positive number
# 0 = zero number
# <0 = negative number

num = int(input("Please enter your number: "))
if num >= 0:
   if  num == 0:
       print("The number is zero.")
   else:
       print("The number is positive.")
else:
    print("The number is negative.")