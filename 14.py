def getRandom2(size1,qty1):
    def getRandom1(size1):
        import random as rd
        rd2=rd.randint(10**(size1-1),(10**size1)-1)
        print(rd2)
    for i  in range(0,qty1):
     getRandom1(size1)
getRandom2(4,20)      

