#Assignment 7
#Q1
import math
C= 50
H = 30
D = []
result =[]
V=input("enter the value of D: ")
D=V.split(",")
D = [int(i) for i in D]
i=0
l = len(D)
while(i<len(D)):
    Q = round(math.sqrt((2*C*D[i])/H))
    result.append(Q)
    i+=1
print("output=",result)

#Q2
class Shape:
    def area(self):
        return 0

class Square (Shape):
    def __init__ (self, l):
        self.l = l
    def area (self):
        return self.l * self.l


c  = Square(12)
print(c.area())

#Q3
class zero:
    def sumzero (self, num):
        for i in range(0,len(num)-2):
            for j in range(i+1, len(num)- 1):
                for k in range(j+1, len(num)):
                    if (num[i] + num[j] + num[k] ==0):
                        print(num[i], num[j], num[k])

test  = zero()
num =  [-25,-10,-7,-3,2,4,8,10]

test.sumzero(num)


#Q5
class Time:
    def addTime (self, hours, mins):
        self.hours = hours
        self.mins = mins
    def displayTime (self):
        print (self.hours, self.mins)

    def displayMinute (self):
        print (self.hours*60 + self.mins)    

obj = Time()
obj.addTime(2,30)

obj.displayTime()
obj.displayMinute()

#Q6
class Person:
    def __init__(self, age):
        if age < 0:
            print("invalid age, setting age to 0")
            self.age = 0
        else:
            self.age = age
    
    def yearpass(self):
        self.age += 1
    
    def amiOld (self):
        if self.age < 13:
            print ("you are young")
        elif self.age >=13 and self.age <=19:
            print("you are a teenager")
        else: 
            print("you are old")

r = Person(24)
r.amiOld()
r.yearpass()
