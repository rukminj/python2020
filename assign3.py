# # Assign 3 
#Q1
print("Q1")
x = [1,3.5,"abe", 4+2j, 7.0,]
print(x)

# #Q2
print("Q2")
l = [1,2,3,4,5]
s = l[0:3]
print(s)

#Q3
l = [1,2,3,4,5]
add = 0
mul = 1
for i in l:
    add = add + i
    mul = mul * i

print("sum is: " , add)
print("multiplication is: ", mul)


#Q4 
print("Q4")
l = [1,0,-4,10,-15,20,5,3,5,4,20,21,21]
high = low = l[0]
for i in l:
    if i > high:
        high = i 
    elif i < low:
        low = i

print("max: ", high)
print("min: ", low)

#Q5
l = [1,2,3,4,5,6,7,8,9,10]
lis = []
for i in range(0,len(l)):
    if l[i]%2 != 0:
        lis.append(l[i])
print("The new list is: ", lis)


#Q7    
l = [1,3,5,7,9,10]
l2 = [2,4,6,8]
l[-1:] = l2
print(l)

#Q8
a={1:10,2:20}
b={3:30,4:40}
c = {}
for i in (a,b): 
    c.update(i)
print(c)

#Q9
d = {}
n = int(input("Enter the size of dictionary: "))
for i in range(1,n+1):
    d[i] = i*i
print (d)

#Q10
x = input("Enter the comma separated values: ")
lis = x.split(",")
tup = tuple(lis)
print(lis)
print(tup)