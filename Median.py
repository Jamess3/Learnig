def median():
# hard program on calculation median
    print('''
    ---------------------------------
    Enter the five number and confirm
    ---------------------------------
    ''')
    number_1 = int(input('Enter number ')) 
    number_2 = int(input('Enter number '))
    number_3 = int(input('Enter number '))
    number_4 = int(input('Enter number '))
    number_5 = int(input('Enter number '))

    sort = [number_1,number_2,number_3,number_4,number_5] # poskladani zadanych cisel 
    sort_middle =sorted(sort) # serazeno od nejmnesiho po nejvetsi hodnota X
    n = len(sort_middle)     # ulozena hodnota pocet number as N
    me = sort_middle[2] # vybrana prostredni hodnota zvana Me as median
    x = (n +1)/2 #Me(x)
    print(f'Me(X) = {x}')
    print (f'''
    {number_1} se od medianu odlisuje o {number_1 - x}
    {number_2} se od medianu odlisuje o {number_2 - x}
    {number_3} se od medianu odlisuje o {number_3 - x} 
    {number_4} se od medianu odlisuje o {number_4 - x}
    {number_5} se od medianu odlisuje o {number_5 - x}
    ''')

median()