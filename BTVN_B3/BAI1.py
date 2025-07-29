from operator import truediv

arr =[]
n = int(input("Nhap so luong ptu n "))
print("Nhap cac phan tu cua mang")
for i in range(n):
    j=int(input())
    arr.append(j)
#2
X=int(input("Nhap X "))
print("So lan xuat hien cua " + str(X) + " la " + str(arr.count(X)))
#3
if n>8 :
    arr[2:7]=[8, 5, 4, 0, 1, 3]
    print("List sau khi thay doi la ", arr)
else :
    print("mang ko du 8 ptu nen ko the thay doi tu 2 den 7 duoc")
#4
max_arr = max(arr)
min_arr = min(arr)
print("so lon nhat trong list la ",max_arr)
print("so nho nhat trong list la ", min_arr)
#5
y=int(input("Nhap so Y tuy chon "))
arr.insert(0,y)
print("List sau khi tren Y vao dau la ", arr)
#6
t=0
for i in range(len(arr)-1):
    if(arr[i]<arr[i+1]):
        t=1
    else:
        t=0
        break
if t==1:
    print("list tang dan ")
d=0
for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        d=1
    else:
        d=0
        break
if d==1:
    print("list giam dan ")
if t==0 and d==0:
    print("list ko dc sap xep ")