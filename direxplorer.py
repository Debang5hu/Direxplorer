import requests
import platform
import os
from time import sleep

def loading_screen():    
        print("""           /^\/^\                                  """)                                                            
        print("""         _|__|  O|                                 """)                 
        print("""\/     /~     \_/ \                                """)
        print(""" \____|__________/  \                              """)
        print("""        \_______      \                            """)
        print("""                `\     \                 \         """)
        print("""                  |     |                  \       """)
        print("""                 /      /                    \     """)
        print("""                /     /                       \\   """)
        print("""              /      /                         \ \ """)
        print("""             /     /                            \  \ """)
        print("""           /     /             _----_            \   \ """)
        print("""          /     /           _-~      ~-_         |   |""")
        print("""         (      (        _-~    _--_    ~-_     _/   |""")
        print("""          \      ~-____-~    _-~    ~-_    ~-_-~    / """)
        print("""            ~-_           _-~          ~-_       _-~  """)
        print("""               ~--______-~                ~-___-~     """)
        print("\n\t\t\t\t\tcreated by: Debangshu Roy")
        print("\n\t\t\t\tA simple Web Directory Scanner made in Python")
        print("--------------------------------------------------------------------------------")
        print("\n")


def clearscreen():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")


def directory_search(address,wordlist):
    with open (wordlist,'r') as fh:
        newaddress=fh.read()
        for x in newaddress.split("\n"):   
            dir=(address + "/" + x)
            response=requests.get("{}".format(dir))
            if(response.status_code==200):
                print("\033[0;32m", "/" + x + "  " + "-> "+ "status: " + str(response.status_code) )
            else:
                print("\033[0m", "/" + x + "  " + "-> "+ "status: " + str(response.status_code) )

if __name__=="__main__":
    clearscreen()
    loading_screen()
    address=input("Enter the url: ")
    wordlist=input("Enter the absolute path of wordlist: ")
    print("\nTarget= {}\nWordlist= {}\n".format(address,wordlist))
    print("Searching...")
    sleep(3)
    directory_search(address,wordlist)
