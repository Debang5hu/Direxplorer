try:
    import platform
    import os
    from loading_screen import loading_screen
    import asyncio
    import aiohttp
except:
    print('[!] Module not found!')


def clearscreen():
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")

async def fetch_response_status(session,url):
    try:
        async with session.get(url) as response:
            return response.status
    except:
        print("\033[1;31m[!] check the URL\033[00m")
        exit(0)


async def directory_search(address,wordlist):
    urllist=[]
    try:
        with open (wordlist,'r') as fh:
            newaddress=fh.read()
            for x in newaddress.split("\n"):   
                try:
                    directory=(address + "/" + x)
                    urllist.append(directory)
                except:
                    pass
    except:
        print("\033[1;31m[!] check the Wordlist file\033[00m")
    async with aiohttp.ClientSession() as session:
        search=[fetch_response_status(session,url) for url in urllist]
        responses=await asyncio.gather(*search)
    
    for x,y in zip(urllist,responses):
        if y in [200,301]:
            print("\033[0;32m",x , " " + "-> " + "status: " , y ,"\033[00m")
        if y == 403:
            print("\033[91m",x , " " + "-> " + "status: " , y ,"\033[00m")
    print('''
==========================================================================================
       DIRECTORY FUZZING COMPLETED
==========================================================================================
''')


if __name__=="__main__":

    clearscreen()
    loading_screen()
    
    address=input("\033[0;34m[*] Enter the url(https://www.example.com): \033[00m")
    wordlist=input("\033[0;34m[*] Enter the absolute path of wordlist: \033[00m")
    
    print('''
==========================================================================================
    \n\033[0;34m[#] Target= \033[1;31m{}\033[0;34m\n[#] Wordlist= \033[1;31m{}\033[0;34m\n[*] Searching...\033[00m
==========================================================================================\n
'''.format(address,wordlist))
    
    
    #directory_search(address,wordlist)
    asyncio.run(directory_search(address,wordlist)) #asyncio
    print("\033[0m")
