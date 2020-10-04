import hashlib, requests, os, time
from colorama import Fore, init
init()

#for clearing the console after the hwid check
clear = lambda: os.system('cls')

def auth():
        #grabs the hwid
        hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

        #hashes the hwid
        hashedhwid = hashlib.sha256(str.encode(hwid)).hexdigest()

        #makes a request to the page where u store the HASHED hwid's , THIS DOES NOT HAVE TO BE PASTEBIN U CAN HOST IT ON YOUR OWN DOMAIN !
        r = requests.get('https://pastebin.com/raw/XXXXXX')

    #checks if the hashed hwid is in the database if it is it continues the code if not it prints the hashedhwid and then quits.
    try:
        if hashedhwid in r.text:
            pass
        else:
            print(f'HWID: {hashedhwid}')
            time.sleep(5)
            exit()
    except:
        print('ERROR')
        exit()

    clear()

auth()

#the main code goes here !
