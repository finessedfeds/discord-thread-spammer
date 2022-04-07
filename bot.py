import requests, threading, random, string, sys, os
from colorama import Fore, Back, Style
import json, time
from colored import fg, attr

class colors:

    darkblue = fg('#1915ed')
    blue = fg('#00ffff')
    aqua = fg('#11d9f0')
    gray = fg('#aab2b3')
    purple = fg('#d400ff')
    ehpurple = fg('#3420e6')


if os.path.exists("tokens.txt"):
    pass
else:
    tokens = open("tokens.txt", "w")
    print(f"{Fore.RED}[-] Input tokens in tokens.txt")
    sys.exit()

valid_tokens = open("valid.txt", "w")

def randomstring():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(5))
    return x

def isvalid(token):
    request = requests.get("https://discordapp.com/api/v6/users/@me/library", headers={'Content-Type': 'application/json', 'authorization': token})
    if request.status_code == 200:
        return True


class Discord():
    
    def createthread(token,name,channelid):
        payload = json.dumps({
        "name": name,
        "type": 11,
        "auto_archive_duration": 60,
        "location": "Thread Browser Toolbar"
        })
        headers = {
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.42 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*'
        }
        url = f"https://discord.com/api/v9/channels/{channelid}/threads"
        while True:
            x = requests.post(url,headers=headers,data=payload)
            if x.status_code == 201:
                print(f'{colors.darkblue}Thread Created.')
            if x.text == "The resource is being rate limited.":                
                bypasslimit = x.json()['retry_after']
                time.sleep(bypasslimit)
                print("Bypassed rate-limit, retrying...")                
                
if __name__ == "__main__":
    os.system("cls||clear")
    tokencount = 0
    for token in open("tokens.txt", "r").read().splitlines():
        tokencount += 1
    validcount = 0
    for token in open("tokens.txt", "r").read().splitlines():
        if isvalid(token) == True:
            valid_tokens.write(token)
            validcount+=1
    print(f"""




    
                                                    {colors.darkblue}╔═╗{colors.aqua}╔═╗{colors.darkblue}╔═╗{colors.aqua}╔╦╗{colors.darkblue}╔╦╗{colors.aqua}╔═╗{colors.darkblue}╦═╗
                                                    {colors.darkblue}╚═╗{colors.aqua}╠═╝{colors.darkblue}╠═╣{colors.aqua}║║║{colors.darkblue}║║║{colors.aqua}║╣ {colors.darkblue}╠╦╝
                                                    {colors.darkblue}╚═╝{colors.aqua}╩  {colors.darkblue}╩ ╩{colors.aqua}╩ ╩{colors.darkblue}╩ ╩{colors.aqua}╚═╝{colors.darkblue}╩╚═

                                                    {colors.gray}$ {colors.darkblue} Thread Spammer {colors.gray}V.1
                                                    {colors.gray}~ {colors.darkblue} {validcount} Tokens
                                                    """)

    channelid = input(f"                                                    {colors.darkblue}Channel ID {colors.gray}-> ")
    threadnames = input(f"                                                    {colors.darkblue}Names {colors.gray}-> ")
    i = 20000000
    for token in open("valid.txt", "r").read().splitlines():
        t = threading.Thread(target=Discord.createthread, args=(token, channelid, threadnames, )).start

    for i in range(int(i) + 1):
        thread = threading.Thread(target=Discord.createthread(token,threadnames,channelid), daemon=True)