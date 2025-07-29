s=str(input("Nhap ho va ten "))
print(s.strip())
a=s.split()
n=len(a)
for i in range(n):
    a[i]=a[i].strip()
    a[i]=a[i].lower()
    a[i]=a[i][0].upper() + a[i][1:]
result = ' '.join(a)
print(result)

