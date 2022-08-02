import colorama, os, time, ctypes
from os import system
from mega import Mega
from colorama import Fore, Style, init
import traceback
colorama.init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW("MEGA.NZ TOOL | MADE BY VLC")

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
checker - check several accounts from txt              
upload - upload a file
creator - accounts creator

If you want to leave when you got an error just restart the programm'''

def upload():
    try:
        mailpass = input(Fore.RED + '\nInput login information(mail:pass) ' + Fore.BLUE)
        try:
            acc = mailpass.split(':')
            mail = acc[0]
            passw = acc[1]
        except:
            print(Fore.RED + '[ERROR] Invalid input')
            upload() 
        try:
            m = mega.login(mail, passw)
        except:
            print(Fore.RED + '[ERROR] Account may be invalid or your internet connection is down')
            upload()
        path = input(Fore.RED + '\nInput path to your file: ' + Fore.BLUE)
        try:
            os.chdir(path)
        except:
            print(Fore.RED + '[ERROR] This path does not exist')
            upload()
        filename = input(Fore.RED + '\nInput filename(example: bebra.txt): ' + Fore.BLUE)
        try:
            file = m.upload(filename)
            print('Success! Link: ' + m.get_upload_link(file))
        except:
            print(Fore.RED + '[ERROR] This file does not exist')
            upload()
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
        try:
            m = mega.login(mail, passw)
            quota = m.get_quota()
            print(f'{Fore.RED}{quota} KB is free')
            balance = m.get_balance()
            print(f'{Fore.RED}Balance is {balance}$')
        except:
            print(Fore.RED + '[ERROR] Account may be invalid or your internet connection is down')
            info()
        input(Fore.RED + '\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\n{Fore.RED}Stopped programm. Exiting...')
        quit()

def ww():
    try:
        amount = int(input(Fore.RED + 'Amount of links you want to generate and check: ' + Fore.BLUE))
        value = 1
        while value <= amount:
            value += 1
    except KeyboardInterrupt:
        print('\n{Fore.RED}Stopped programm. Exiting...')
        quit()

def checker():
    valid = 0
    invalid = 0
    try:
        path = input(Fore.RED + '\nInput path to txt with accounts: ' + Fore.BLUE)
        try:
            os.chdir(path)
        except:
            print(Fore.RED + '[ERROR] This path does not exist')
            checker()
        file = input(Fore.RED + '\nInput filename(example: bebra): ' + Fore.BLUE)
        try:
            f = open(f'{file}.txt', 'r')
            f.close()
        except:
            print('[ERROR] This file does not exist')
            checker()
        input(Fore.RED + 'Press enter to start checker')
        with open(f'{file}.txt', 'r', encoding='utf-8') as accounts:
            accounts = accounts.read()
            if len(accounts) >= 1:
                account = accounts.split('\n')
        for account in account:
            try:
                acc = account.split(':')
                mega.login(acc[0], acc[1])
                print(f"{Fore.LIGHTGREEN_EX}[VALID] {account}")
                output = open('validmega.txt', 'a', encoding='utf-8')
                output.write(account + '\n')
                output.close()
                valid += 1
            except:
                print(f"{Fore.RED}[INVALID] {account}")
                invalid += 1
        print(f'''
Check finished.
Valid accounts: {Fore.LIGHTGREEN_EX}{valid}{Fore.RESET}
Invalid accounts: {Fore.RED}{invalid}{Fore.RESET}
Total accounts: {valid+invalid}''')
        input(Fore.RED + '\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\n{Fore.RED}Stopped programm. Exiting...')
        quit()

def creator():
    print(Fore.WHITE + 'https://github.com/vlc1337/meganzaccountcreator (also read readme for this soft)')
    input(Fore.RED + '\nPress enter to continue.')

while True:
    cls()
    print(logo)
    try:
        select = str(input(Fore.RED + '\nInput command: ' + Fore.BLUE))
        if select == 'upload':
            upload()
        elif select == 'info':
            info()
        elif select == 'checker':
            checker()
        elif select == 'creator':
            creator()
        else:
            print(Fore.RED + '\nCommand does not exist. ')
            nextCode = input('\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\nError')
        print('\nStopped programm. Exiting...')
        quit()
