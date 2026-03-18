#list is used to store multiple values in one variable
# example:num=[10,20,30]
#Instead a=10,b=20,c=30
# In python, a list can be stores different types of elements(not only similar elements)

#to print different types of element 
data=[10,"hello",35.65,True]
print(data)

#change number which is already declared
num=[9,3,8,2,5]
print(num)
num[2]=1
print(num)

#print only mentioned index value
nums=[31,41,51,61]
print("number of index 1 is:",nums[1])

#loop through list
num=[10,20,30,40]
for i in num:
    print(i)

#Append
number=[10,20,30]
number.append(40)
print(number)    

#remove element
a=[10,20,30,40]
a.remove(30)
print(a)

#lenght of a list
num=[10,20,30,40,50]
print("lenght is:",len(num))

#joining of list
a=[10,20,30]
b=[40,50,60]
c=a+b
print(c)

#find large num
num=[30,10,50,80]
print(max(num))

#sum of list
a=[10,20,30,40]
sums=0
for i in a:
    sums=sums+i
print(sums)

#sum of num
a=[10,20,30,40]
print("sum of list:",sum(a))