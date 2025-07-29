from operator import truediv

s1=str((input("Nhap chuoi s1 ")))
s2=str((input("Nhap chuoi s2 ")))
rv_s1 = s1[::-1]
print(rv_s1)
print("do dai s2 la ",len(s2))
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
if 1<=a<b<=len(s2):
    rv_2 = s2[a:b+1][::-1]
    rv_s2=s2[:a]+rv_2+s2[b+1:]
    print("s2 sau khi nghich dao tu ",a," den ",b," la ",rv_s2)
else:
    print("a va b ko hop le ")
#
s3=""
for i in range(len(s1)):
    if(i%2==0):
        continue;
    else:
        s3+=s1[i]
print("s3 la ", s3)
#
cs1=1
cs2=0
j=0
k=0
s4=""
while j<len(s1) and k<len(s2):

    if cs1==1 and j<len(s1):
        s4+=s1[j]
        j+=1
        cs1=0
        cs2=1
    elif cs2==1 and j<len(s2):
        s4+=s2[k]
        k+=1
        cs2=0
        cs1=1
if j<len(s1):
    s4+=s1[j:]
elif k<len(s2):
    s4+=s2[k:]
print("s4 la ", s4)
