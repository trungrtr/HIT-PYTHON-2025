list1=list()
print("Nhap cac ptu huy nhap hay an khac so")
while True:
    x=input()
    if x.isnumeric():
        list1.append(x)
    else:
        break
print(list1)
tuple=tuple(list1)
print (tuple)

for i in tuple:
    temp=i
    count_tuple=tuple.count(i)
   # print(count_tuple)

    if count_tuple % 5 == 0 and count_tuple % 10 != 0:
        print(i)

    temp=i
    if i==temp:
        continue







