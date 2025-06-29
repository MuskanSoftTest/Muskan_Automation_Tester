# a <= b and a <=c small numbers
# b >=a and b >=c large numbers
# c <= b and c >=a small number

a= 10
b=90
c=76

# find the smallest number
if a <= b and a <= c:
    print("smallest number is {}".format(a))
elif b <= a and b <= c:
    print("smallest number is {}".format(b))
else:
    print("smallest number is {}".format(c))


# find the largest number
if a >= b and a >= c:
    print("largest number is {}".format(a))
elif b >= a and b >= c:
    print("largest number is {}".format(b))
else:
    print("largest number is {}".format(c))