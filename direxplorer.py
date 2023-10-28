#!/bin/bash/python3

# _*_ coding: utf-8 _*_

#only shows the 200 and 301 directories
#usage [python3 direxplorer.py -w /usr/share/wordlists/dirb/common.txt -u http://www.example.com]

try:
    import sys,getopt
    import asyncio
    import aiohttp
except:
    print('[!] Module not found!')

def loading_screen():
   print('''
 ____________________
| Direxplorer v:0.1  |
  ===================
    \t\033[0;34mWeb Directory Scanner\033[00m made in \033[0;34mPython\033[00m : \033[0;34m@Debang5hu\033[00m

''')
    



async def fetch_response_status(session,url):
    try:
        async with session.get(url) as response:
            return response.status
    
    except TimeoutError:
        print("\033[1;31m[!] Timeout Error!\033[00m")
        return
    
    except aiohttp.ClientError as e:
        print("\033[1;31m[!] Error while fetching {url}: {e}\033[00m")
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

        # ok: 200  redirect: 301 (http status code)
        if y in [200,301]:
            print("\033[0;32m",x , " " + "-> " + "status:" , y ,"\033[00m")

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
