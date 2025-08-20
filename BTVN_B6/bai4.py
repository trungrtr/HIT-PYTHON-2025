def phone(s):
    phone=''
    for i in s:
        if i.isdigit():
            phone+=i
    if phone[0]!='0':
        print("loi")
    elif len(phone)!=10:
        print("loi")
    else:
        print(phone)
phone("0123a456.789")
phone("123a45ddada890")
phone("098aaaa7654a321")

