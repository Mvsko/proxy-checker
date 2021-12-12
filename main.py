from pyfiglet import Figlet
import urllib.request , socket
import time;
from os import system
import os

pcsname = "Proxy Checker"

t = time.localtime()
timenow = time.strftime("%H:%M:%S", t)
clear = lambda: os.system('cls')
clear()
system("title " + pcsname)

f = Figlet(font='slant')
print(f.renderText(pcsname))

socket.setdefaulttimeout(180)

proxynumber = input("Combien de proxies voulez-vous vérifier ?: ")

try:
    val = int(proxynumber)
except ValueError:
    print("Vous devez insérer un nombre !")
    time.sleep(3)
    exit()

proxyList = []

for i in range(int(proxynumber)):
    nmb = i+1
    proxyqst = input("[" + str(nmb) + "]" + " Insérer le proxy à vérifier (ip:port): ")
    proxyList.append(proxyqst)

print()

def proxycheck(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        socket=urllib.request.urlopen('http://google.com/')
    except urllib.error.HTTPError as e:        
        print('[Erreur] ', timenow ,'- Code:', e.code)
        return e.code
    except Exception as detail:

        print("[Erreur]", timenow, '-', detail)
        return 1
    return 0

for proxy in proxyList:
    if proxycheck(proxy):
        print (">> [" + proxy + "]", timenow , "- Ce proxy ne fonctionne pas ou est inexistant.")
    else:
        print (">> [" + proxy + "]", timenow , "- Ce proxy est actuellement fonctionnel")
        
time.sleep(4)