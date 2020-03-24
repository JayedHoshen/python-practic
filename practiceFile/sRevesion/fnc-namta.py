while True:
    def nam_cal(nam_number=1):
        i = 1
        while i <= 10:
            print(nam_number,"x",i,"=",nam_number*i)
            i +=1
    nam_number= input("Enter any number that calculate namta:")
    nam_number = int(nam_number)
    nam_cal(nam_number)
