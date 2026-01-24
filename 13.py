f1=open("in1.txt","r")
f2=open("out1.txt","w")
s1=f1.readline()
list1=s1.split(",")
n1=int(list1[0])
n2=int(list1[1])
for j in range(n1,n2+1):
    for i in range(1,11):
        print(j,"l",i,j*i)
        f2.write("karthik")
        f2.write("/n")
    f2.write("/n")
    print()
f2.close()
                 
