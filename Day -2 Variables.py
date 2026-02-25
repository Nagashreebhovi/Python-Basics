# what is variable?
# Variable is a container used to store data.

# types of variable datatypes
# 1.interger -- ex:age=12 , students=45
# 2.string --   ex: name="nagashree"  college="DSCE" // we shoud declare string using double quotes"""
# 3.character -- ex: dog=d  name= p //only single character
# 4.float -- ex: height=5.5  weight=45.50 
# 5.dictionary --ex:student={"name":"arun" "age"=20} //key-value pair
# 6.boolean --ex: is_student=true  //true or false
# 7.list --ex: marks=[80,50,60,70]\

# simple code using variables
a=10
b=50
print("sum=",a+b)

#using f string
student1="anu"
student2="madhu"
print(f"both {student1} and {student2} are friends")

#student data
name="Arpita"
age=15
is_student=True
print(f"name of the student: {name} age is :{age} {is_student} she is a student")

# swap 2 numbers using f string
a=50
b=20
print(f"before swapping a={a} b={b}")
a,b=b,a
print(f"after swapping a={a} b={b}")

# swap 2 numbers using temp logic
a=10
b=20
print("before swap",a,b)
temp=a
a=b
b=temp
print("after swap",a,b)

#to find the square and cube of a number
num=30
square=num*num
print("square of a number",square)

num=5
cube=num*num*num
print("cube of a number",cube)

#another way to find 
num=5
square=num**2
print("square",square)

num=5
cube=num**3
print("cube",cube)

num=int(input("enter number"))
square=num**2
print("square value is:",square)

#sum of 2 num
num1=int(input("enter number:"))
num2=int(input("enter second num:"))
sum=num1+num2
print("sum of 2 num is",sum)

# find average
sub1=int(input("enter maths marks:"))
sub2=int(input("enter English marks:"))
sub3=int(input("enter Hindi marks:"))
avg=sub1+sub2+sub3/3
print("average marks is:",avg)

#swapping numbers taking input
a=int(input("enter num1:"))
b=int(input("enter num 2:"))
print("before swap:",a,b)
a=temp
a=b
temp=b
print("after swap:",a,b)

#calculate percentage
a=int(input("enter kannada marks"))
b=int(input("enter English marks"))
c=int(input("enter Hindi marks"))
d=int(input("enter Maths marks"))
e=int(input("enter Science marks"))
f=int(input("enter Social marks"))
total=a+b+c+d+e+f
avg=(a+b+c+d+e+f)/6
perc=(total/600)*100
highest=max(a,b,c,d,e,f)
print("average",avg)
print("percentage",perc)
print("highest marks",highest)

# grade based on percentage
a=int(input("enter kannada marks"))
b=int(input("enter English marks"))
c=int(input("enter Hindi marks"))
d=int(input("enter Maths marks"))
e=int(input("enter Science marks"))
f=int(input("enter Social marks"))
total=a+b+c+d+e+f
perc=(total/600)*100
print("percentage",perc)
if perc >=80:
    print("grade A")
elif perc >=60:
    print("grade B")
elif perc >35:
    print("grade C")
else:
    print("Fail")
