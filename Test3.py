def name_func(b):
    b=b.lower()
    return [ord(i)-96 for i in b if " " ] 
Name="My name is Vachagan"
print(name_func(Name))