#Task-1(a)
============================================================
# Python program to check if the input number is prime or not



b = 407
b = int(input("Enter a number: "))


if b > 1:
   
   # check for factors
   
   for i in range(2,b):
       
       if (b % i) == 0:
           
           print(b,"is not a prime number")
           
           print(i,"times",b//i,"is",b)
           
           break
   
else:
       
       print(b,"is a prime number")
  



#Task-1(b)
=============================================================
#Printing Prime Numbers by Defining funcrion
print "===Prime Numbers Witmething (an object) back to the call so you can use ith Definations==="

count = 0
def prime(x):
    if x >= 1:

        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True

a=int(raw_input("enter starting num :"))	        
b=int(raw_input("enter ending num :"))

for i in range(a,b):
    if prime(i):
        count += 1
        print i

print "Total Prime nums are ",count
