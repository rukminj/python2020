#Q1
try:
    x
except:
    print("syntax error")

#Q3
x = []
x = input("enter 4 digits: ")
while(len(x) != 4):
    x = input("String is too long/short, please provide 4 digits: ")

#Q4
print("Enter the username and password: ")

count = 0
while count <= 3:
    user = input("Enter the username: ")
    password = input("enter the password: ")

    if password == "abd2331" and user == "abcd":
        print("user and password is correct")
        break
    else: 
        count +=1
        print("Try again; Attempts remaining: " , 3-count)
        

#Q5
fobj = open("file.txt")
test = fobj.read()
test1 = test.split(" ")
print(test1)
x = []
for i in test1:
    if(len(i%2!=0)):
        print(i)


   