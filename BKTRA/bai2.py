n=int(input("nhap so pt cua list "))
print("nhap cac ptu cua list ")
list=list()
for i in range(n):
    x=str(input())
    list.append(x)
set1=set()
for i in range(n):
    for j in range(len(list[i])):
        set1.add(list[i][j])

print(set1)