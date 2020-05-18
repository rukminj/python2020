# Q1
a,b,c = 10, 6.4, "string"
print("Q1")
print ( a,b,c)

#Q2
x, y  = 10 + 4j, 10
print ("Q2")
print("Before swap", x, y)
x,y = y,x
print("After swap", x, y)


#Q3
a,b = 10,20
print ("Q3")
print ("Before swap", "a =", a, ", b =", b)
result = a 
a = b 
b = result 
print ("After Swap", "a =", a, ", b =", b)

a,b = 10,20
print ("Q3 part 2")
print ("Before swap", "a =", a, ", b =", b)
a,b = b,a
print ("After Swap", "a =", a, ", b =", b)

#Q4
print ("Q4")
a = input("Enter the value:")
print ("Q4 input value is : ")

# python2: a = raw_input("Enter the value:")

#Q5
print("Q5")
a = int(input("Enter a number between 1 to 10:"))
b =int(input("Enter a number between 1 to 10:"))
z = a + b
print("The sum is: ", z)

z += 30
print("The sum +30 is: ", z )


#Q6
x = input("Enter input: ")
print ("The input value data type is: ", type(x))

#Q7

AreaOfSquare = 5.6 # Upper Camel Case
areaOfSquare = 5.6 # Lower Camel Case
area_of_square = 5.6 #snake case



#Q8
#Yes the value of a will change as the new value will overwrite a 
# The memory location of a will also change