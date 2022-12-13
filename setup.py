#!/usr/bin/env python3

import signal, socket, os, shutil, git
from simple_term_menu import TerminalMenu
from colorama import Fore

def sig_handler(sig, frame):
  print('\n[*] Exiting...\n')
  exit(1)

signal.signal(signal.SIGINT, sig_handler)

def install_csgo(ip):
  print(Fore.RESET + '\nInstalling CSGO\n')
  steamaccount = input(Fore.RED + '-> '+ Fore.LIGHTRED_EX + 'Write steamaccount: ')
  print(Fore.MAGENTA + '[*] Installing Dependences ...')

  os.system('sudo dpkg --configure -a')
  os.system('sudo apt install steamcmd -y')
  os.system('sudo add-apt-repository multiverse')
  os.system('sudo dpkg --add-architecture i386')
  os.system('sudo apt update')
  os.system('sudo apt install lib32gcc1 steamcmd -y')

  print(Fore.BLUE + '[*] Installing CSGO ...')

  if(os.path.exists('./Steam')):
      shutil.rmtree('./Steam')
  os.mkdir('Steam')
  os.system('./Steam/steamcmd.sh +login anonymous +force_install_dir ~/cs_go/ +app_update 740 validate +quit')

  print(Fore.RED + '[*] Coping CFG Files ...')

  with open('./logaddress.cfg', 'r') as r:
    logaddress_file = r.read().replace('xxx.xxx.xxx.xxx', ip)
  with open('~/cs_go/csgo/cfg/logaddress.cfg', 'w') as w:
    w.write(logaddress_file)
  with open('./cfg/esl5on5.cfg', 'rb') as r:
      esl5on5_cfg = r.read().replace('{steamaccount}', steamaccount)
  with open('~/cs_go/csgo/cfg/esl5on5.cfg', 'wb') as w:
      w.write(esl5on5_cfg)
  with open('./cfg/gotv.cfg', 'rb') as r, open('~/cs_go/csgo/cfg/gotv.cfg', 'wb') as w:
      w.write(r.read())
  with open('./cfg/autoexec.cfg', 'rb') as r, open('~/cs_go/csgo/cfg/autoexec.cfg', 'wb') as w:
      w.write(r.read())
  
  print(Fore.YELLOW + '[*] Coping Start Server Script ...')

  with open('./scripts/startserver.sh', 'r') as r:
    startserver_file = r.read().replace('xxx.xxx.xxx.xxx', ip).replace('{steamaccount}', steamaccount)
  with open('~/cs_go/startserver.sh', 'w') as w:
    w.write(startserver_file)
    
  print(Fore.RESET + '\nCSGO Installed Correctly!!!\n')

def install_ebot(ip):
  print(Fore.RESET + '\nInstalling EBOT\n')
  print(Fore.MAGENTA + '[*] Installing Docker Compose ...')

  os.system('sudo apt install docker-compose')

  print(Fore.BLUE + '[*] Downloading Docker Ebot ...')

  if(os.path.exists('./docker-ebot')):
      shutil.rmtree('./docker-ebot')
  git.Git('./docker.ebot').clone('https://github.com/jffz/docker-ebot.git')
  with open('./docker-ebot/docker-compose.yml', 'r') as r:
    docker_file = r.read().replace('xxx.xxx.xxx.xxx', ip)
  with open('./docker-ebot/docker-compose.yml', 'w') as w:
    w.write(docker_file)

  print(Fore.RED + '[*] Installing Docker Ebot ...')

  os.system('sudo docker-compose up -d ./docker-ebot/docker-compose.yml')

  print(Fore.RESET + '\nEBOT Installed Correctly!!!\n')

def main():
  options = ['Install CSGO and ebot', 'Install CSGO', 'Install ebot']

  hostname = socket.gethostname() 
  ip = socket.gethostbyname(hostname)

  terminal_menu = TerminalMenu(
    options, 
    title = '\nKyubiful CSGO Server Installation\n', 
    menu_cursor_style=['fg_red', 'bold'], 
    menu_highlight_style=['underline'], 
    status_bar_style=['bg_red'],
    menu_cursor='-> '
  )
  
  menu_entry_index = terminal_menu.show()

  if(menu_entry_index == 0):
    install_csgo(ip)
    install_ebot(ip)
    exit(0)
  if(menu_entry_index == 1):
    install_csgo(ip)
    exit(0)
  if(menu_entry_index == 2):
    install_ebot(ip)
    exit(0)

if __name__ == "__main__":
    main()