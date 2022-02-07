import imp
import sys
import colorama
from os import system
from colorama import Fore, Style, init
from pyfiglet import Figlet

MORSE_CODE_DICT = { 'A':'.-',       'B':'-...',         'C':'-.-.',     'D':'-..', 
                    'E':'.',        'F':'..-.',         'G':'--.',      'H':'....',
                    'I':'..',       'J':'.---',         'K':'-.-',      'L':'.-..', 
                    'M':'--',       'N':'-.',           'O':'---',      'P':'.--.', 
                    'Q':'--.-',     'R':'.-.',          'S':'...',      'T':'-',
                    'U':'..-',      'V':'...-',         'W':'.--',      'X':'-..-', 
                    'Y':'-.--',     'Z':'--..',
                    
                    '1':'.----',    '2':'..---',        '3':'...--',    '4':'....-',    '5':'.....',
                    '6':'-....',    '7':'--...',        '8':'---..',    '9':'----.',    '0':'-----', 
                    
                    ',':'--..--',   '.':'.-.-.-',
                    '?':'..--..', 
                    '/':'-..-.', '-':'-....-',
                    
                    '(':'-.--.', ')':'-.--.-'
                    }
 
################################################## MAIN ##################################################

def main():
    
    system ('cls')
    init()

    banner = Figlet(font='banner3-D')
    print(Fore.YELLOW + banner.renderText(' Morse') + Style.RESET_ALL)

    print('\n')

    print(
        Fore.RED + ' [1] ' + Fore.WHITE + 'Text to Morse code\n' +
        Fore.RED + ' [2] ' + Fore.WHITE + 'Morse code to Text'
    )
    
    main_input = input(Fore.GREEN + " >> ")
    
    if main_input == '1':
        TexttoMorse()
    elif main_input == '2':
        MorsetoText()
    else:
        pass

################################################## TEXT to MORSE ##################################################

def TexttoMorse():
    
    system('cls')
    
    print()
    
    text = input(Fore.RED + " [TEXT] " + Fore.LIGHTYELLOW_EX)
    
    text = text.upper()
    
    print()
    
    cipher = ''
    
    for i in text:
        if i != ' ':
            cipher += MORSE_CODE_DICT[i] + ' '
        
        else:
            cipher += ' '
            
    print(Fore.GREEN + " [MORSE] " + Fore.LIGHTCYAN_EX + cipher)
    
    print()
    
    print(Fore.WHITE + " Back to Main ? (y/n) ")
    answer = input(Fore.RED + " >> ")
    if answer == 'y' or answer == 'Y':
        main()
    else:
        pass
    
################################################## MORSE to TEXT ##################################################

def MorsetoText():
    system('cls')
    
    print()
    
    morse = input(Fore.RED + " [MORSE] " + Fore.LIGHTYELLOW_EX)
    
    morse = morse.upper()
    
    print()
    
    morse += ' '
    decipher = ''
    citext = ''
    
    for i in morse:
        if i != ' ':
            j = 0
            citext += i
            
        else:
            j += 1
            
            if j == 2:
                decipher += ' '
            else:
                decipher += list( MORSE_CODE_DICT.keys() )[list( MORSE_CODE_DICT.values() ).index(citext)]
                citext = ''
      
    print(Fore.GREEN + " [TEXT] " + Fore.LIGHTCYAN_EX + decipher)
    
    print()
    
    print(Fore.WHITE + " Back to Main ? (y/n) ")
    answer = input(Fore.RED + " >> ")
    if answer == 'y' or answer == 'Y':
        main()
    else:
        pass
      
################################################## BODY ##################################################

main()