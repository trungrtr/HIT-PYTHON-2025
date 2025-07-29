k = int(input("Nhap so luong phan tu cua list "))
arr = []
for i in range(k):
    a=int(input())
    arr.append(a)
n=int(input("Nhap n "))
m=int(input("Nhap m "))
if n*m<=k:
    X = []
    index=0;
    for i in range(n):
        list=arr[index:index+m]
        X.append(list)
        index=index+m
    print("Mang X la ", X)
else:
    print("NO")
