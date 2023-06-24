import colorama, os, time, ctypes, datetime, random, string
from os import system
from datetime import datetime
from mega import Mega
from colorama import Fore, Style, init
import traceback
from datetime import datetime

colorama.init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW("MEGA.NZ TOOL | MADE BY VLC | VERSION 0.3")

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
                                
checker - check several accounts from txt              
upload - upload a file
massupload - upload a file to several accs
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
            print(Fore.RED + '\n[ERROR] Invalid input')
            upload() 
        try:
            m = mega.login(mail, passw)
        except:
            print(Fore.RED + '\n[ERROR] Account may be invalid or your internet connection is down')
            upload()
        path = input(Fore.RED + '\nInput path to your file: ' + Fore.BLUE)
        try:
            os.chdir(path)
        except:
            print(Fore.RED + '\n[ERROR] This path does not exist')
            upload()
        filename = input(Fore.RED + '\nInput filename(example: bebra.txt): ' + Fore.BLUE)
        try:
            file = m.upload(filename)
            print('\nSuccess! Link: ' + m.get_upload_link(file))
        except:
            print(Fore.RED + '\n[ERROR] This file does not exist')
            upload()
        input(Fore.RED + '\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\nStopped programm. Exiting...')
        quit()

def checker():
    valid = 0
    invalid = 0
    try:
        path = input(Fore.RED + '\nInput path to txt with accounts: ' + Fore.BLUE)
        try:
            os.chdir(path)
        except:
            print(Fore.RED + '\n[ERROR] This path does not exist')
            checker()
        file = input(Fore.RED + '\nInput filename(example: bebra.txt): ' + Fore.BLUE)
        try:
            f = open(f'{file}', 'r')
            f.close()
        except:
            print('\n[ERROR] This file does not exist')
            checker()
        input(Fore.RED + '\nPress enter to start checker')
        start_time = datetime.now()
        with open(f'{file}', 'r', encoding='utf-8') as accounts:
            accounts = accounts.read()
            if len(accounts) >= 1:
                account = accounts.split('\n')
        for account in account:
            try:
                acc = account.split(':')
                driver.get("https://mega.nz/login")
                login_input = driver.find_element_by_name("email")
                login_input.send_keys(acc[0])
                password_input = driver.find_element_by_name("password")
                password_input.send_keys(acc[1])
                if "MY ACCOUNT" in driver.title:
                   print(f"{Fore.LIGHTGREEN_EX}[VALID] {account}")
                   valid += 1
                else:
                    print(f"{Fore.RED}[INVALID] {account}")
                    invalid += 1
                driver.quit()
            except:
                print(f"{Fore.RED}[INVALID] {account}")
                invalid += 1
        print(f'''
Check finished.
Valid accounts: {Fore.LIGHTGREEN_EX}{valid}{Fore.RESET}
Invalid accounts: {Fore.RED}{invalid}{Fore.RESET}
Total accounts: {Fore.MAGENTA}{valid+invalid}{Fore.RESET}
Time passed: {Fore.MAGENTA}{datetime.now() - start_time}{Fore.RESET}
Valid accounts saved in the same path as the accounts''')
        input(Fore.RED + '\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\n{Fore.RED}Stopped programm. Exiting...')
        quit()

def massupload():
    success = 0
    err = 0
    try:
        path = input(Fore.RED + '\nInput path to txt with accounts: ' + Fore.BLUE)
        try:
            os.chdir(path)
        except:
            print(Fore.RED + '\n[ERROR] This path does not exist')
            massupload()
        file = input(Fore.RED + '\nInput filename with accounts(example: bebra.txt): ' + Fore.BLUE)
        try:
            f = open(f'{file}', 'r')
            f.close()
        except:
            print('\n[ERROR] This file does not exist')
            massupload()
        path = input(Fore.RED + '\nInput path to the file you want to upload: ' + Fore.BLUE)
        try:
            os.chdir(path)
        except:
            print(Fore.RED + '\n[ERROR] This path does not exist')
            massupload()
        filename = input(Fore.RED + '\nInput filename(example: bebra.txt): ' + Fore.BLUE)
        try:
            f = open(f'{file}', 'r')
            f.close()
        except:
            print('\n[ERROR] This file does not exist')
            massupload()
        input(Fore.RED + '\nPress enter to start mass upload')
        start_time = datetime.now()
        with open(f'{file}', 'r', encoding='utf-8') as accounts:
            accounts = accounts.read()
            if len(accounts) >= 1:
                account = accounts.split('\n')
        for account in account:
            try:
                acc = account.split(':')
                z = mega.login(acc[0], acc[1])
                file = z.upload(filename)
                z.get_upload_link(file)
                print(f'{Fore.WHITE}Account: {Fore.GREEN}{account} {Fore.WHITE}Link to uploaded file: {Fore.GREEN}{z.get_upload_link(file)}')
                output = open('uploadedlinks.txt', 'a', encoding='utf-8')
                output.write(z.get_upload_link(file) + '\n')
                output.close()
                success += 1
            except:
                print(f"{Fore.RED}[ERROR] Account: {account}")
                err += 1
        print(f'''
Mass upload finished.
Success: {Fore.LIGHTGREEN_EX}{success}{Fore.RESET}
Errors: {Fore.RED}{err}{Fore.RESET}
Time passed: {Fore.MAGENTA}{datetime.now() - start_time}{Fore.RESET}
Links to the files saved in the same path as the accounts''')
        input(Fore.RED + '\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\n{Fore.RED}Stopped programm. Exiting...')
        quit()

def creator():
    print(Fore.WHITE + '\nhttps://github.com/vlc1337/meganzaccountcreator (also read readme for this soft)')
    input(Fore.RED + '\nPress enter to continue.')

while True:
    cls()
    print(logo)
    try:
        select = str(input(Fore.RED + '\nInput command: ' + Fore.BLUE))
        if select == 'upload':
            upload()
        elif select == 'checker':
            checker()
        elif select == 'creator':
            creator()
        elif select == 'massupload':
            massupload()
        else:
            print(Fore.RED + '\nCommand does not exist. ')
            nextCode = input('\nPress enter to continue.')
    except KeyboardInterrupt:
        print('\nError')
        print('\nStopped programm. Exiting...')
        quit()
