try:
    import platform
    import os,sys,getopt
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
            print("\033[0;32m",x , " " + "-> " + "status:" , y ,"\033[00m")
        if y in [403]:
            print("\033[0;31m",x , " " + "-> " + "status:" , y ,"\033[00m")
    print('''
==========================================================================================
       DIRECTORY FUZZING COMPLETED
==========================================================================================
''')



if __name__=="__main__":

    clearscreen()
    loading_screen()

    #argv
    #target_url=sys.argv[1]
    #target_wordlist=sys.argv[2]

    arguments=sys.argv[1:]

    try:
        args,null=getopt.getopt(arguments,"u:w:",["url=","wordlist="])
        for x,y in args:
            if x in ['-u','--url']:
                target_url=y
            if x in ['-w','--wordlist']:
                target_wordlist=y
            
    except:
        print("\033[0;31m[#] Error Encounted!\033[00m")
    
    print('''
==========================================================================================
    \n\033[0;34m[#] Target= \033[1;31m{}\033[0;34m\n[#] Wordlist= \033[1;31m{}\033[0;34m\n\033[00m
==========================================================================================\n
'''.format(target_url,target_wordlist))
    
    
    #directory_search(address,wordlist)
    asyncio.run(directory_search(target_url,target_wordlist)) #asyncio
