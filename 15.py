country=[]
capital=[]
mark=[]
f1=open("file.txt","r")

for i in range(0,10):
    
    line1=f1.readlines().strip()
    list1=line1.split(",")
    country.append(list1[0])
    capital.append(list1[1])

for i in range(0,3):
    r1=input("what is cap of "+country[i])
    if r1.lower()==capital[i].lower():
        mark.append(10)
    else:
        mark.append(0)
    print(mark)
    print(sum(mark))
    
