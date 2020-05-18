# # Q1
print("Q1")
x = int(input("Enter a number: "))
if x % 3 == 0 and x % 5 ==0 :
    print("Consultadd Python Training")
elif x % 3 == 0:
    print("Consultadd")
elif x % 5 == 0:
    print("c")
else:
    print("the number is not divisible by 3 or 5")

# #Q2
print("Q2")

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
print("Enter an operation:")
print("1 - addition; 2 - substraction; 3 - division; 4 - multiplication; 5 - average")
c = int(input("Enter the choice:"))
if c !=5:
    if c == 1:
       result = (x+y)
    elif c == 2:
        result = (x-y)
    elif c == 3:
        result =(x/y)
    elif c == 4:
        result =(x*y)
elif c == 5: 
    x = int(input("Enter a number for average: "))
    y = int(input("Enter a number for average: "))
    result =((x+y)/2)

print(result)
if result < 0 :
    print("result is negative")

# #Q3
print("Q3")

a,b,c = 10,20,30
avg = (a+b+c)/3
print("avg = ", avg)
if avg >a and avg > b and avg > c:
    print("avg is higher than a,b,c")
elif avg > a and avg > b:
    print("avg is higher that a,b")
elif avg > a and avg > c:
    print("avg is higher that a,c")
elif avg > b and avg > c:
    print("avg is higher than b,c ")
elif avg > a :
    print("avg is higher than a")
elif avg > b:
    print("avg is just higher than b")
elif avg > c:
#     print ("avg is higher than c")


# # Q4
print("Q4")
while True:
    i = int(input("Enter a number, negative number to exit"))
    if i >= 0 :
        print("Good Going")
        continue
    else:
        print("Its over")
        break

# print("Q5")
i = 2000

while i >= 2000 and i <= 3200:
    if i % 7 == 0 and i % 5 != 0:
        print (i)
    i += 1

# #Q7
print("Q7")
i = 0
while i<=6
    if i != 3 and i != 6:
        print(i)
    i += 1




#Q8
print("Q8")
x = str(input("Enter a string"))
digits = letters = 0
for c in x:
    if c.isdigit():
        digits += 1
    elif c.isalpha():
        letters += 1
print("Letters: ", letters)
print("digits: ", digits)

#Q9
print("Q9 part 1")
lucky = 8
x = int(input("Guess lucky number: "))
while x != lucky:
    x = int(input("Try again: "))
print ("you guessed the lucky number")

# print("Q9 part 2")
lucky = 8
number = int(input("Guess the lucky number: "))
if(number != lucky):
    answer = input("Would you like to try again, 'no' to end: ")
    while number!= lucky and answer!="no":
        number = int(input("Guess the lucky number: "))
        if number != lucky:
            answer = input("Would you like to try again, 'no' to end: ")


#Q10
print ("Q10")
counter = 1
lucky = 8
while counter <= 5:
    number = int(input("Guess the lucky number: "))
    if number == lucky:
        print ("good guess")
    else: 
        print ("try again")
    counter += 1
    
#Q11
print("Q11")
counter = 1
lucky = 8
while counter <= 5:
    number = int(input("Guess the lucky number: "))
    if number == lucky:
        print ("good guess")
        break
    else: 
        print ("try again")
    counter += 1



        
        