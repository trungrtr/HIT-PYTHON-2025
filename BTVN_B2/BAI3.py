n =int(input("Nhap so "))
dem=int
dem=0
sum=int
sum=0
while n>0:
    sum+=n%10
    dem+=1
    n=n//10
print("so chu so la "+ str(dem) +"tong cac so la "+str(sum))