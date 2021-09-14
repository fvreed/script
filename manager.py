from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Modullar yüklənir...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    '   _____         .__                   ',
    '  /  _  \ ___.__.|  |__ _____    ____',
    '/    |    \___  ||   Y  \/ __ \|   |  \ ',
    '\____|__  / ____||___|  (____  /___|  /',
    '        \/\/          \/     \/     \/ ',
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GENISYS==============')
    print(f'   Versiya: 1.2 | Sahibi: Ayhan{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Yeni hesablar əlavə et'+n)
    print(lg+'[2] Bütün qadağan edilmiş hesabları silin'+n)
    print(lg+'[3] Xüsusi hesabları silin'+n)
    print(lg+'[4] Çıxış et'+n)
    a = int(input('\nSeçiminizi edin: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Əlavə ediləcək hesabların sayını daxil edin: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Əlavə ediləcək telefon nömrəsini daxil edin: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Bütün hesablar qeyd edildi!')
            clr()
            print(f'\n{lg} [*] Yeni hesablara giriş edilir..\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Giriş uğurludur!')
                c.disconnect()
            input(f'\n Ana menyuya qayıtmaq üçün enteri basın...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Hesab yoxdur! Zəhmət olmasa bir hesab əlavə edin və yenidən cəhd edin.')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} ban edilməyib!{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' ban edilib!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Təbriklər! Qadağan edilmiş hesab yoxdur')
                input('\nAna menyuya qayıtmaq üçün enteri basın...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] Bütün qadağan edilmiş hesablar silindi'+n)
                input('\nAna menyuya qayıtmaq üçün enteri basın...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Silmək üçün bir hesab seçin\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Seçiminizi edin: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Hesab silindi{n}')
        input(f'\nAna menyuya qayıtmaq üçün enteri basın...')
        f.close()
    elif a == 9:
        print(f'\n{lg}[i] Checking for updates...')
        try:
            # https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt')
        except:
            print(f'{r} You are not connected to the internet')
            print(f'{r} Please connect to the internet and retry')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Downloading updates...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/add.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Cryptonian007/Astra/main/manager.py')
                print(f'{lg}[*] Updated to version: {version.text}')
                input('Press enter to exit...')
                exit()
            else:
                print(f'{lg}[!] Update aborted.')
                input('Press enter to goto main menu...')
        else:
            print(f'{lg}[i] Your Astra is already up to date')
            input('Press enter to goto main menu...')
    elif a == 4:
        clr()
        banner()
        exit()
