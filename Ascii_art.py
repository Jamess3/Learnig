#First, you need to install FIGlet to VSC  --- (VCS - Visual Studio Code)
#Write to terminal ------ pip install pyfiglet----- (install pyfiglet to VSC)
import pyfiglet # uplaud FIGlet from VCS
print ('Change text or word to ASCII art')
text = str(input('Write text\n')) # write text, which will show
change = pyfiglet.figlet_format(text, font='smisome1') # figlet_format - change text to ascii art (text)/ # font=  ASCII art  font type
print(change)
print(""" \nASCII art font type -\n3-d\ncalgphy2\nacrobatic\nalligator\navatar\nbasic\ncricket\natd. """)