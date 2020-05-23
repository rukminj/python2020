new_list=[1,2,3,3,4,5,2,1]
x = []
for i in new_list:
    if i not in x:
        x.append(i)
    else:
        pass

print (x)

# new = []
# l = [new.append(i) for i in new_list if i not in new x.append]

#new_list=[1,2,3,3,4,5,2,1]
#output--> [1,2,3]

# lis1=[1,2,3,4,5,6,6,5,7,8]
# #r=[list[i] for i in list if list[i]=list[i+1]]
# r=[]
# for j in (0,range(len(list))):
#     if(lis1[j]==lis1[j+1]):
#         r.append(lis1[j])


# new=[]
# var=[new.append(i) for i in [1,2,3,3,4,5,2,1] if i not in new]
# print(new)