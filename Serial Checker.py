try:
    from os import system, getenv, path, name
    if name != 'nt':
        print(f"\n [*] The '{name}' os system is not allowed.")
        exit()
    else:
        pass
    from subprocess import check_output
    from time import sleep
    from ctypes import windll
    from sys import stdout, exit, argv, executable
    from colored import fg
    from requests import get
    import pyautogui
    import win32com.shell.shell as shell
except ModuleNotFoundError:
    def md(prnt):
        for ryuk in prnt:
            stdout.write(ryuk)
            stdout.flush()
            sleep(0.005)
        print()
    def AutoInstall():
        system("title Module Installation...")
        system("pip install pywin32")
        system("pip install colored")
        system("pip install requests")
        system("pip install pyautogui")
        system("cls")
        system("title Installation complete")
    md(f"[+] Missing Modules")
    md(f"[#] Auto-Installation in process. Please wait...");AutoInstall()
    from colored import fg
    md(f"{fg(9)}[#] {fg(7)}Modules installed.\n{fg(9)}[+] {fg(7)}Please restart the program")
    system("title Please restart the program.")
    system("pause>nul")
    exit()

system("cls");system("title WMIC SerialNumber Checker")

def dprint(text):
    for ryuk in text:
        stdout.write(ryuk)
        stdout.flush()
        sleep(0.005)
    print()

ADMIN_PERMISSION = windll.shell32.IsUserAnAdmin() == 1

if not ADMIN_PERMISSION:
    try:
        ASADMIN = 'asadmin'
        if argv[-1] != ASADMIN:
            script = path.abspath(argv[0])
            params = ' '.join([script] + argv[1:] + [ASADMIN])
            shell.ShellExecuteEx(lpVerb='runas', lpFile=executable, lpParameters=params)
    except:
        system('Mode Con Cols=50 Lines=4')
        dprint(f"\n {fg(9)}[!]{fg(7)} Please enable administrator permission.")
        system('pause>nul')
        exit()

system('Mode Con Cols=47 Lines=4')
print(f"\n {fg(9)}[#]{fg(7)} Press OK in the messagebox to continue.")
windll.user32.MessageBoxW(None, '© AkaTool\'s - ! "ℛყ𝖚K̭̭̏ (j\'ai sauté)#7475\nhttps://github.com/AkaDevloppement\nPress OK to continue.', 'Credits', 1+64)
latailedemabite = 0
system('cls')
system('Mode Con Cols=30 Lines=4')
while True:
    print(f"\n {fg(118)}[/]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    print(f"\n {fg(119)}[-]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    print(f"\n {fg(120)}[\]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    print(f"\n {fg(121)}[|]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    print(f"\n {fg(122)}[/]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    print(f"\n {fg(123)}[-]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    print(f"\n {fg(122)}[\]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    print(f"\n {fg(121)}[|]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    print(f"\n {fg(120)}[*]{fg(7)} Loading informations...");sleep(0.065);system('cls')
    latailedemabite = latailedemabite + 1
    if latailedemabite == 3:
        try:
            ipv4 = get("https://httpbin.org/ip").json()
            ipv6 = get("https://api64.ipify.org/").text
            networkstatus = 0
        except: 
            networkstatus = 1
        break
    else:
        pass

system('Mode Con Cols=78 Lines=40')
pc = check_output('wmic diskdrive get SystemName').decode().split('\n')[1].strip()
model = check_output('wmic csproduct get Name').decode().split('\n')[1].strip()
hwid = check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
seriald = check_output('wmic diskdrive get serialnumber').decode().split('\n')[1].strip()
bios = check_output('wmic bios get serialnumber').decode().split('\n')[1].strip()
volume = check_output('wmic logicaldisk get VolumeSerialNumber').decode().split('\n')[1].strip()
cpu = check_output('wmic cpu get serialnumber').decode().split('\n')[1].strip()
baseboard = check_output('wmic baseboard get serialnumber').decode().split('\n')[1].strip()
ram = check_output('wmic memorychip get serialnumber').decode().split('\n')[1].strip()

if networkstatus == 1:
    dprint(f"\n {fg(9)}[+]{fg(7)} IPV4: None | (network error)")
    dprint(f"\n {fg(9)}[+]{fg(7)} IPV6: None | (network error)")
else:
    dprint(f"\n {fg(9)}[+]{fg(7)} IPV4: "+ipv4['origin'])
    dprint(f"\n {fg(9)}[+]{fg(7)} IPV6: "+ipv6)
dprint(f"\n {fg(9)}[+]{fg(7)} Computer Name: "+pc)
dprint(f"\n {fg(9)}[+]{fg(7)} Computer Model: "+model)
dprint(f"\n {fg(9)}[+]{fg(7)} Windows Session Username: "+getenv('username'))
dprint(f"\n {fg(9)}[#]{fg(7)} HWID: "+hwid)
dprint(f"\n {fg(9)}[#]{fg(7)} SERIAL DISK: "+seriald)
dprint(f"\n {fg(9)}[#]{fg(7)} BIOS: "+bios)
dprint(f"\n {fg(9)}[#]{fg(7)} CPU: "+cpu)
dprint(f"\n {fg(9)}[+]{fg(7)} VOLUME: "+volume)
dprint(f"\n {fg(9)}[#]{fg(7)} BASEBOARD: "+baseboard)
dprint(f"\n {fg(9)}[#]{fg(7)} RAM: "+ram)
dprint(f"\n {fg(9)}[+]{fg(7)} MAC ADRESS: ");sleep(0.5);print(system('getmac'))
sleep(2)
dprint(f"\n {fg(9)}[%]{fg(28)} Press enter to exit.");system('pause>nul')
exit()
