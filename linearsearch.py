list=[1,5,6,7,9,0]
number=int(input("Please enter the number:"))
for i in list:
    if i==number:
        print("True its match")
        break
else:
    print("No Match to List")


for i in range(0,len(list)):
    if list[i]==number:
        print("index of number",i)
        break
else:
    print("NO index in list")