# #Q1
# x = [10, 20.5, 6+4j,"abc", "a", 5-7j, 4.8, 6 , "asd", 10]
# #Q2
# y = x[1:6]
# print(y)
# #Q3
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# print(x[5][0:4])
# print(x[6:8])
# print(x[-3:-1])

# # Q4
# x = [range(0,1000)]

#Q6

# for i in range(0,100):
#     if i%3 == 0 and i %2 == 0:
#         print (i)


#Q7
# st = input("Enter a string: ")
# vow = {"index":0, "vowel": "a"}
# rev = st[::-1]
# print("reverse string is: ", rev)
# for i in range(0,len(rev)):
#     if rev[i] == "a" or rev[i] == "e" or rev[i] =="i" or rev[i] =="o" or rev[i] =="u":
#         vow["index"] = i
#         vow["vowel"] = rev[i]
#         print(vow)


#Q8
st = "hello my name is abcde"
ls = st.split(" ")
for j in range(0,len(ls)):
    if len(ls[j]) %2 == 0:
        print(ls[j])
   

#Q9
x=[1,2,3,4,5,6,7,8,9,-1]
s = 8
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i] + x[j] == s:
            print (x[i], x[j])


#Q9
even_list = odd_list = []
x = int(input("Enter a number in the range of 1:50: "))
