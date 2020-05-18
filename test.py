x = str(input("Enter a string"))
d = {"digits": 0, "letters": 0}
for c in x:
    if c.isdigit():
       d["digits"] += 1
    elif c.isalpha():
       d["letters"] +=1
print(d)