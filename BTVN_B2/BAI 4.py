N=int(input("Nhap so xu "))
T=int
t=int
s=int
if(N<28):
    print("Ko mua dc chai nao ")
else:
    T=int(N/28)
    t=int(T/3)
    s=t+T
    print("So chai bia mua dc la "+ str(s))