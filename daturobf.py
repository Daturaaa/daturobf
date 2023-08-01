import base64
import os
import fade
from colorama import Fore, Style
import sys
from time import sleep
import datetime
import string
import random
import random

letters = string.ascii_letters
numbers = string.digits
confuse = letters + numbers + string.punctuation

fr = datetime.datetime.now()
currenttime = fr.strftime('%H:%M:%S')
print(currenttime)

def lprint(_str):
    for letter in _str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.04)


def obf():
    os.system('cls')
    logo = '''
 ______        ____   ,---------.   ___    _ .-------.        ,-----.     _______    ________  
|    _ `''.  .'  __ `.\          \.'   |  | ||  _ _   \     .'  .-,  '.  \  ____  \ |        | 
| _ | ) _  \/   '  \  \`--.  ,---'|   .'  | || ( ' )  |    / ,-.|  \ _ \ | |    \ | |   .----' 
|( ''_'  ) ||___|  /  |   |   \   .'  '_  | ||(_ o _) /   ;  \  '_ /  | :| |____/ / |  _|____  
| . (_) `. |   _.-`   |   :_ _:   '   ( \.-.|| (_,_).' __ |  _`,/ \ _/  ||   _ _ '. |_( )_   | 
|(_    ._) '.'   _    |   (_I_)   ' (`. _` /||  |\ \  |  |: (  '\_/ \   ;|  ( ' )  \(_ o._)__| 
|  (_.\.' / |  _( )_  |  (_(=)_)  | (_ (_) _)|  | \ `'   / \ `"/  \  ) / | (_{;}_) ||(_,_)     
|       .'  \ (_ o _) /   (_I_)    \ /  . \ /|  |  \    /   '. \_/``".'  |  (_,_)  /|   |      
'-----'`     '.(_,_).'    '---'     ``-'`-'' ''-'   `'-'      '-----'    /_______.' '---'                                                                                             
'''
    print(fade.purplepink(logo))
    file = str(input(f'''{Fore.MAGENTA + Style.BRIGHT}
Drag and drop your file here! (●'◡'●)
{Fore.WHITE}┌─[{Fore.MAGENTA}datura@obf{Fore.WHITE}]
└>>{Fore.MAGENTA} ''')).replace(fr'//', '/').replace('"', '')
    
    if '.py' not in file:
        lprint(f'{Fore.RED + Style.BRIGHT}[-] File has to be a .py file!')
        sleep(3)
        quit()
    
    elif '.py' in file:
        lprint(f'{Fore.GREEN + Style.BRIGHT}[+] File is valid!')
        os.system('cls')
        print(fade.purplepink(logo))
        with open(file, 'rb') as e:
            e = e.read()
            obf1 = base64.b64encode(e)
            print(f'{Fore.GREEN}[+] Obfuscated with b64')
            obf2 = base64.b85encode(obf1)
            print('[+] Obfuscated with b85')
            obf3 = base64.b32encode(obf2)
            print('[+] Obfuscated with b32')
            obf4 = base64.b16encode(obf3)
            print('[+] Obfuscated with b16')
            obf5 = base64.b64encode(obf4)
            print('[+] Obfuscaeted with b64')
            obf6 = base64.b85encode(obf5)
            print('[+] Obfuscated with b85')
            with open('./obfuscated.py', 'w') as i:
                i.write('import base64\n')
            print('[*] Generating Fake Webhooks')
            sleep(1)
            for i in range(5000):
                idz = []
                striz = []
                flowerz = []

                for strii in range(68):
                    stri = random.choice(letters)
                    striz.append(stri)

                for idd in range(19):
                    id = random.choice(numbers)
                    idz.append(id)

                for flowerr in range(100):
                    flower = random.choice(confuse)
                    flowerz.append(flower)

                hook = str(f'https://discordapp.com/api/webhooks/{idz}/{striz}').replace(' ', '').replace('\'', '').replace('[', '').replace(']', '').replace(',', '')
                print(f'[+] {hook}')
                with open('./obfuscated.py', 'a') as i:
                    i.write(f'\nwebhook{random.randint(100000,999999)} = "{hook}"\n# {striz}{striz}{striz}{striz}{striz}')
                        
            str1 = f'exec(base64.b64decode(base64.b85decode(base64.b32decode(base64.b16decode(base64.b64decode(base64.b85decode({obf6})))))))'
            with open('./obfuscated.py', 'a') as i:
                i.write(f'\n{str1}')

            print(f'{Fore.MAGENTA}[+] Successfully obfuscated \'{file}\' -> ./obfuscated.py')
            sleep(5)
            obf()
obf()