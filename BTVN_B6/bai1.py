a = lambda a,b:(chr(ord(a)+1) if a!='z' else 'z',chr(ord(b)+1) if b!='z' else 'z')
print(a('z','a'))