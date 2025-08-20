def mt(x,*arg):
    if x=="add":
        rs=0
        for i in arg:
            rs+=i
        print("sum = ",rs)
    elif x=="multiply":
        rs=1
        for x in arg:
            rs*=x
        print("tich = ",x)
    elif x=="max":
        rs=max.arg
        print("max = ", rs)
    elif x=="min":
        rs=min.arg
        print("min = ",rs)
    else:
        print("Invalid operation")
def main():
    x=str(input("Nhap vao yeu cau "))
    mt(x,1,2,3,4)
main()