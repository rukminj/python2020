# Assignment 6
#Q1
x = list(filter(lambda x: x%3!=0 and x%7==0, range(1,50)))
print(x)

#Q2
def multiply(x):
    return x*x

x = list(map(multiply,range(1,10)))
print(x)

#Q3
test = "isUpPerCase"
x = [i for i in test if i.isupper()==True]
print(x)

#Q4
student = ['smit', 'jaya','rayyan']
course = ['CSE', 'Networking', 'Operating System']

d = dict()
for i in range(0,len(student)):
    d[student[i]] = course[i]
print ("using loops: ",d)
dc = {student:course for(student,course) in zip(student,course)}
print("using dictionary comprehension: ", dc)


#Q6
def revstr(mystr):
    yield mystr[::-1]

x = revstr("ConsultaddTraining")
print(list(x))