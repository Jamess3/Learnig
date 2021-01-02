again = True
while(again):
    print('Enter the palidrome')
    palidrome = str(input(''))
    first_word = palidrome[0]
    last_word = palidrome[-1]
    if first_word == last_word:
        print('Yes, it is a palindrome')
    else:
        print('No, it\'s not a palindrome')
    again = input('Do you want continue? y/n\n')
    if again.startswith('Y') or again.startswith('y'):
        again = True
    else:
        again = False

print('Thanks you >-]')