import requests
import platform
import os
from time import sleep
from loading_screen import loading_screen


def clearscreen():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")


def directory_search(address,wordlist):
    with open (wordlist,'r') as fh:
        newaddress=fh.read()
        for x in newaddress.split("\n"):   
            try:
                dir=(address + "/" + x)
                response=requests.get("{}".format(dir))
                if(response.status_code==200) or (response.status_code==301):
                        print("\033[0;32m", "/" + x + "  " + "-> "+ "status: " + str(response.status_code) )
                else:
                        print("\033[0m", "/" + x + "  " + "-> "+ "status: " + str(response.status_code) )
            except:
                 pass

if __name__=="__main__":
    print("\033[0m")
    clearscreen()
    loading_screen()
    address=input("[*] Enter the url(https://www.example.com): ")
    wordlist=input("[*] Enter the absolute path of wordlist: ")
    print("\n[#] Target= {}\n[#] Wordlist= {}\n".format(address,wordlist))
    print("[*] Searching...\n")
    sleep(3)
    directory_search(address,wordlist)
    print("\033[0m")
