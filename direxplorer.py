#!/bin/bash/python3

try:
    import sys,getopt
    from loading_screen import loading_screen
    import asyncio
    import aiohttp
except:
    print('[!] Module not found!')




async def fetch_response_status(session,url):
    try:
        async with session.get(url) as response:
            return response.status
    except:
        print("\033[1;31m[!] check the URL\033[00m")
        return  #this keyword saved a lot of errors


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
        print("\033[1;31m[!] check the Path of the Wordlist\033[00m")
        return
    
    #here where the concept starts
    async with aiohttp.ClientSession() as session:
        search=[fetch_response_status(session,url) for url in urllist]
        responses=await asyncio.gather(*search)

    
    for x,y in zip(urllist,responses):
        #instance() method works like a comparison operator
        if isinstance(y, Exception): 
            print('[+] An Error Occurred!')
            pass
        if y in [200,301]:
            print("\033[0;32m",x , " " + "-> " + "status:" , y ,"\033[00m")
        if y in [403]:
            print("\033[0;31m",x , " " + "-> " + "status:" , y ,"\033[00m")

    #footer
    print('''
===========================================================================
DIRECTORY FUZZING COMPLETED
===========================================================================
''')


def main():
    if sys.hexversion >= 0x03080000:
        #banner
        loading_screen()


        #cli input
        try:
            arguments=sys.argv[1:]
            args,null=getopt.getopt(arguments,"u:w:",["url=","wordlist="])

            for x,y in args:
                if x in ['-u','--url']:
                    target_url=y
                if x in ['-w','--wordlist']:
                    target_wordlist=y

            
        except:
            print("\033[0;31m[#] Error Encounted!\033[00m")
    
        print('''
===========================================================================
\033[0;34m[#] Target: \033[1;31m{}\033[0;34m\n[#] Wordlist: \033[1;31m{}\033[0;34m\033[00m
===========================================================================
'''.format(target_url,target_wordlist))
    
    
        #directory_search(address,wordlist)
        asyncio.run(directory_search(target_url,target_wordlist)) #asyncio
    
    else:
        sys.exit('[+] Required Python Version > 3.8!')


if __name__=="__main__":
    #main function    
    main()
