#loops repeate a block of code multiple times
#types of loops 
#for loop :when you know how many times to repeate
#while loop:


# print number from 0-10
for i in range(11):
    print(i)

# print num from 1-10
for i in range(1,11):
    print(i)

#print 5 times hii
for i in range(1,6):
    print("hii",i)  

#print name 5 times
for i in range(5):
    print("Nagu")

#print reverse num
for i in range(10,0,-1):
    print(i)

#print even num
for i in range(2,21,2):
    print(i)

#print odd num
for i in range(1,20,2):
    print(i)

#sum
sum=0
for i in range(1,11):
    sum=sum+i
print("sum=",sum)

#print table from taking input num
num=int(input("enter num"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    
#check prime number
num=int(input("enter num"))
count=0
for i in range(1,num+1):
    if num%2==0:
        print