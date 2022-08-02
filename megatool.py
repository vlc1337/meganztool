import colorama, os, time
from os import system
from mega import Mega
from colorama import Fore, Style, init
colorama.init(autoreset=True)

cls = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')
mega = Mega()

logo = f''' 
 {Fore.MAGENTA} ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄    ▄▀▀█▄    ▄▀▀▄ ▀▄  ▄▀▀▀▀▄        ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄     
 {Fore.BLUE} █  █ ▀  █ ▐  ▄▀   ▐ █         ▐ ▄▀ ▀▄  █  █ █ █ █     ▄▀      █    █  ▐ █      █ █      █ █    █      
 {Fore.LIGHTBLUE_EX} ▐  █    █   █▄▄▄▄▄  █    ▀▄▄    █▄▄▄█  ▐  █  ▀█ ▐ ▄▄▀▀        ▐   █     █      █ █      █ ▐    █      
 {Fore.LIGHTGREEN_EX}   █    █    █    ▌  █     █ █  ▄▀   █    █   █    █              █      ▀▄    ▄▀ ▀▄    ▄▀     █       
 {Fore.YELLOW} ▄▀   ▄▀    ▄▀▄▄▄▄   ▐▀▄▄▄▄▀ ▐ █   ▄▀ ▄ ▄▀   █      ▀▄▄▄▄▀      ▄▀         ▀▀▀▀     ▀▀▀▀     ▄▀▄▄▄▄▄▄▀ 
 {Fore.LIGHTRED_EX} █    █     █    ▐   ▐         ▐   ▐    █    ▐          ▐      █                             █        
{Fore.RED} ▐    ▐     ▐                           ▐                      ▐                             ▐         

                            {Fore.WHITE} >>> https://github.com/vlc1337 <<<
                            
info - get information about account                      
upload - upload a file'''

def upload():
    try:
        mailpass = input(Fore.RED + '\nInput login information(mail:pass) ' + Fore.BLUE)
        acc = mailpass.split(':')
        mail = acc[0]
        passw = acc[1]
        m = mega.login(mail, passw)
        path = input(Fore.RED + '\nInput path to your file: ' + Fore.BLUE)
        os.chdir(path)
        filename = input(Fore.RED + '\nInput filename(example: bebra.txt): ' + Fore.BLUE)
        file = m.upload(filename)
        print(m.get_upload_link(file))
        input(Fore.RED + '\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\nStopped programm. Exiting...')
        quit()

def info():
    try:
        mailpass = input(Fore.RED + '\nInput login information(mail:pass) ' + Fore.BLUE)
        acc = mailpass.split(':')
        mail = acc[0]
        passw = acc[1]
        m = mega.login(mail, passw)
        quota = m.get_quota()
        print(f'{Fore.RED}{quota} KB is free')
        balance = m.get_balance()
        print(f'{Fore.RED}Balance is {balance}$')
        input(Fore.RED + '\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\n{Fore.RED}Stopped programm. Exiting...')
        quit()

while True:
    cls()
    print(logo)
    try:
        select = str(input(Fore.RED + '\nInput command: ' + Fore.BLUE))
        if select == 'upload':
            upload()
        elif select == 'info':
            info()
        else:
            print(Fore.RED + '\nCommand does not exist. ')
            nextCode = input('\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\nError')
        print('\nStopped programm. Exiting...')
        quit()
