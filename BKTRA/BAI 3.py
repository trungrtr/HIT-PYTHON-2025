n=int(input("so ptu cua ham "))
print("nhap cac ptu cua list a")
a=list()

for i in range(n):
 x=int(input())
 a.append(x)

b=list()
a.sort()
b.append(a[n-1]+1)


for i in range(1,n):
    # a.random(1,9)
    b.append(b[i-1]+1)
print("phan tu nho nhat cua bn la ",b[0])
print(b)