#check positive negative
num = int(input("enter num:"))
if num > 0:
    print("possitive")
else:
    print("negative")


# check even odd
num=int(input("enter num"))
if num%2==0:
    print("even number")
else:
    print("odd nunber")

# find largest of 3 number
a=int(input("enter 1 number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a==b==c:
    print("all are equal")
elif a>=b and a>=c:
    print("a is greater")
elif b>=a and b>=c:
    print("b is greater")
else:
    print("c is greater")

#check range between 1-50
a=int(input("enter num"))
if 1<a and 50>a:
    print("in range")
else:
    print("not in range")
    