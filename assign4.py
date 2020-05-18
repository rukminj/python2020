#Assign4
def reverse(str):
    rev = ''
    i = len(str)
    while i>0:
        rev += str[i-1]
        i -=1
    return rev
print(reverse("1234abcd"))

#Q2
def case(x):
    num = {"upper": 0, "lower":0 , "other": 0}
    for i in x:
        if i.isupper() == True:
           num["upper"] += 1
        elif i.islower() == True:
            num["lower"] += 1 
        else:
            num["other"] += 1
    return num

print(case("Test123"))


#Q3
def unique(list):
    new = []
    for i in list:
        if i not in new:
            new.append(i)
    return new
unique([1,5,5,3,5,4,8,5,8,1453,564,4,5,5])

#Q4
def sort(str):
    list = str.split('-')
    list.sort()
    return('-'.join(list))

print(sort("this-is-a-test"))

#Q5
def cap(str):
    return(str.upper())

x = input("Enter a string: ")
print(cap(x))

#Q6

def sum(a,b):
    a = int(a)
    b = int(b)
    return (a+b)

print(sum("10", "20"))

#Q7
def maxlen(a,b):
    if len(a) > len(b):
        print(a)
    elif len(a) < len(b):
        print(b)
    else:
        print(a)
        print(b)

maxlen("test", "test")

#Q8
def square():
    print(tuple(map(lambda x: x**2, range(0,21))))

square()

#Q9
def showNumbers(limit):
    for i in range(1,limit+1):
        if i %2==0:
            print(i,"EVEN")
        elif i%2 != 0:
            print(i, "ODD")

showNumbers(12)

#Q10 
print( list(filter(lambda x: x%2 ==0, range(1,21))))

#Q11
l = [1,2,3,4,5,6,7,8,9,10]
m =list( map(lambda x: x**2, l))
num = list(filter(lambda x: x%2==0, m))
print(num)

# Q12
try:
    x = 5/0
except:
    print("divide by 0")

#Q13
from functools import reduce
l = [[1,2,3],[4,5],[6,7,8]]
print (reduce(lambda x, y : x+y,l))

