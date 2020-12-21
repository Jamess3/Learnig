def food():
#middle program on 
    ovoce = 'malina','jahoda','banan'
    zelenina = 'okurka','salat','rajce'
    jidlo = True
    print('###############################################')
    print('VÌTEJ V PROGRAMU NA ROZPOZNÀNÌ OVOCE A ZELENINY')
    print('###############################################')
    while jidlo:
        print ('''    
    Na  vyber mas 
rajce/ salat / banan
okurka / jahoda/ malina
    --------------------------------''')
        prvek = input('Napis ovoce nebo zelenina\n')
        if prvek in ovoce:
            print('Zadal jsi ovoce')
            pokracovat = str(input('Prejes si zadat dalsi slovo? ano/ne\n'))
            if pokracovat == 'ne':
                if prvek == ovoce[2]:
                    print(f'Zadal jsi {prvek} ktery ma  {len(prvek)} slov')
                else:
                    print(f'Zadal jsi {prvek} ktera ma  {len(prvek)} slov')
                break
        elif prvek in zelenina:
            print('Zadal jsi zeleninu')
            pokracovat = str(input('Prejes si zadat dalsi slovo? ano/ne\n'))
            if pokracovat == 'ne':
                if prvek == zelenina[2] or zelenina[1] :
                    print(f'Zadal jsi {prvek} ktery ma  {len(prvek)} slov')
                else:
                    print(f'Zadal jsi {prvek} ktera ma  {len(prvek)} slov')
                break
        else:
            print('''-------------------------
    POZOR!!!! NENI V SEZNAMU
    ------------------------
            ''')

food()