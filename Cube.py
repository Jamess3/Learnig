from random import randrange, choice # Generuje nahodne cisla, slov
################## nahodne vybere podle pismena zenske povolani (ulozeno do definice)
def woman():
    job = choice(['a','b','c','d','e'])
    if job == 'a':
        print('''
Žena plačka

Církev vyhradila ženám péči o zesnulé a oplakávání.        
''')
    elif  job == 'b':
        print('''
Žena matka

Ženy v produktivním věku  stále těhotné  + starost o kojence. 
Vysoká úmrtnost novorozenců, polovinu svého plodného věku žena čeká dítě nebo rodí. 
Stará se o dům a domácnost, když je náhodou vše hotovo, doporučuje se tkaní a vyšívání, 
činnosti bez konce.       
''')
    elif  job == 'c':
        print('''
Žena řemeslníka

míň práce, nutná šetrnost a počestnost. 
Domácnost pod silným mravním dohledem.        
''') 
    elif job == 'd':
        print('''
Žena urozená

musí vést velkou domácnost, ale zproštěna manuální práce i výchovy dětí relativní volnost, 
věnuje se zábavám a někdy umění. Na hradech vznikají komnaty pro hradní dámy + jejich doprovod = fraucimor. 
Domlouvané svatby, hlavní slovo má příbuzenstvo. Sňatek často ukončuje soupeření rodů. 
Urozená žena zažívá mnohem větší nesvobodu, nakládá se s ní jako s prostředkem prosazení politických a majetkových zájmů rodiny.
Už od narození se pro ni hledal vhodný partner a pokud z dohody sešlo, nebo dívka byla nedejbože "příliš ošklivá", 
odklidila se do kláštera, aby svůj prvotní hřích smyla věčným panenstvím. 
Urozená dáma o sobě mohla začít sama rozhodovat de fakto až ve chvíli, kdy ovdověla. 
Vdovské věno jí zaručilo ekonomickou nezávislost a pokud byla ještě svěží, 
klidně se mohla znovu provdat za muže, kterého si sama zvolila.       
''')
    else:
        print('''
Žena  - idol dvorské lásky

Doba trubadůrů a rytířských turnajů, od 12.st. Platonický vztah s rytířem, 
vítězi věnuje část svého šatu - šátek, rukáv, kapesník, rytíř ho připevní na kopí. 
Obraz ženy jako křehké vázičky potřebující ochranu se zrodil až v představách potulných rytířů, 
kteří pěli milostné písně pod okny nepracujících šlechtičen.       
''')
#################### konec vyberu zenskeho povolani

####################zacatek programu uvod
print('''
---HELLO EVERYONE WELCOME TO THE GAME ---
 -----------ROLL THE DICE----------------

This game generates functions from the librery SECRET,
which also used by spy organization. >-)
And bonus!!! By name. I'll show yo, what was your job
in a past life.
OK let's GOOOO !!! 
''')
####################konec uvodu
print('As first put your noble name please:')
player_1 = input('') # zeptat se na jmeno
#################### vyber je zenske jmeno 
if player_1.endswith('a') or player_1.endswith('e'):
    print(f'''
hello {player_1} this is beautiful name and do you want to know, 
what did you do ;-] yes/no''')
    past_women = input('')
    if past_women == 'yes':
        woman() # definice povolani
    else:
        pass

     
##################### vyber je muzske jmeno  
elif player_1: 
    print(f'''
Yeeaaa   silent everywhere THE KING IS BACK Hi dude.
{player_1} is name for KING, you must write yes,
for your job >-]
''')
    past_men = str(input(''))
    if past_men == 'yes':
        print('Was your job is? Press enter')
        print('''
Byl jsi CHASNÍK sorry bro 
V Čechách byl chasník obyčejně tovaryš od řemesla, 
při němž bývalo více chasy, na př. sladovnický chasník, 
řeznický chasník a p. Význam »mladý muž« je obvyklý na Moravě, 
kde chasa znamená svobodný, mladý lid obojího pohlaví; 
v krajích, kde »chasa« jsou děti, je chasník (chasníček) 
názvem malého dítěte (na Valašsku). 
TAK SNAD JSI Z MORAVY :-D
''')
        input('Press enter for contineu')
    else:# zadani bylo ne 
        pass

############### Zacatek hrat kostky
print ('Ok, finally let\'s Go, PLAY')

game = True
while game:
    input('Press enter for Roll of the dice')
    throw_1 = randrange(1,7)# vybere prvni hod
    print(f'Your first throw is {throw_1}')
    input ('Press enter for second Roll of dice')
    throw_2 = randrange(1,7)#vybere druhy hod
    print(f'Your second throw is {throw_2} and result {throw_1 + throw_2}')
    stop = input('Do you want to quit? For stop press \'no\', for continue, press any key\n')
    if stop == '':
        continue
    elif stop == 'no':
        game = False

print('Thanks you for GAME -- Roll of the dice')
        
        
