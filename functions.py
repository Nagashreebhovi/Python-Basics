#function is a block of code that can be performed specific task and can be used again and again.
# instead of writing the same code many times we put it inside a function.
#two types of functions 
# 1.built-in function
# these are already provided by python. we dont create then we just use them.
# some common built in functions are:
#print()
#len()
#type()
#input()
#range()

#def is a keyword used to create a function.def stands for "define"
#use break - when you want to stop the loop
#use return- when you want to stop the function

# structure to print
def welcome():
    print("welcome to dsce")
welcome()

#calling many times
def greet():
    print("Good morning")
greet()
greet()
greet()

#build-in function of len
def dog():
    print(len("dogs are loyal"))
dog()
#taking input from user and count length
a=input("enter name:")
print("length:",len(a)) 
    
#built-in function of type
def salary():
    print(type(90000.90))
salary()    

#built in function using range
def num():
    for i in range(1,10):
        print(i)
num()    
#counting vowels
word=input("enter word:")
vowels="aeiou"
count=0
for ch in word:
    if ch in vowels:
        count=count+1
print("vowels",count)

#print 1-n
def numbers(n):
    for i in range(1,n+1):
        print(i)
num=int(input("enter num:"))
numbers(num)

#function to print multiplication table
def table():
    num=int(input("number:"))
    for i in range(1,11):
        print(i*num)
table()
#parameters passing to check largest of two num
def num(a,b):
    if (a>=b):
        print("a is larger",a)
    else:
        print("b is larger",b)
a=input("enter 1st num");
b=input("enter 2nd number");
num(a,b)

#check prime or not
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(" not prime")
            return
    print("prime")
num=int(input("enter num to check prime:"))
prime(num)
  
# factorial of a number
def fact(n):
    fact=1
    for i in range(1,n+1):#repeats the process from 1 to n
        fact=fact*i   #it multiplies the current factorial value by the number i each time
    return fact       #it retuns the value back to the function
n=int(input("enter number:"))
result=fact(n)
print("fact num",result)

#polindrome
def pol(n):
    if n==n[::-1]:
        return "polindrome"
    else:
        return "not polindrome"
num=input("enter num:")
res=pol(num)
print(res)