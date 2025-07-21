T=int(input("Nhap tien luong "))
thue=float
thunhap=float
if(T>15):
    thue=T*0.3
    thunhap=T-thue
    print("Thue: " + str(thue) + " Thu nhap: " + str(thunhap))
elif(T>=7 and T<=15):
    thue=T*0.2
    thunhap= T- thue
    print("Thue: " + str(thue) + " Thu nhap: " + str(thunhap))
else:
    thue=T*0.1
    thunhap = T - thue
    print("Thue: " + str(thue) + " Thu nhap: " + str(thunhap))