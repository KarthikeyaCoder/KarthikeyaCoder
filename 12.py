ifile=
open("file1.txt","r")
l=[]


for line in ifile:
    temp=int(line.replace("/n",""))
    l.append(temp)

for j in l:
    for i in range(1,11):
        print(i,"x",j,"=",i*j)
    print("")
        
    
             
