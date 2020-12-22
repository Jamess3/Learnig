import random
name = str(input('Enter name\n'))
for sign in name:
    if ord(sign) in range (1,127):
        cesar = ord(sign) + random.randint(1,4)
        if (cesar > 119): 
           cesar = cesar - random.randint(5,10)
        final = chr(cesar)
        print(final, end= '')
