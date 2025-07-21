t = int(input("Nhập tháng "))
n = int(input("Nhập năm "))
if(t==2):
    if(n%4==0):
        print("co 29 ngay")
    else:
        print("co 28 ngay")
elif(t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12):
    print("co 31 ngay")
else :
    print("co 30 ngay")
