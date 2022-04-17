## Bored so wrote this script to automatically setup my pc for fresh windows installs

import os
import platform
from playsound import playsound
import keyboard as kb
import time 
import admin
import ctypes, sys
import winapps



windows = '''


                  .,,uod8B8bou,,.
                    ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
               ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
               !...:!TVBBBRPFT||||||||||!!^^""'   ||||
               !.......:!?|||||!!^^""'            ||||
               !.........||||                     ||||
               !.........||||    Setting Up       ||||
               !.........||||                     ||||
               !.........||||    unofficialdxnny  ||||
               !.........||||                     ||||
               !.........||||                     ||||
               `.........||||                    ,||||
                .;.......||||               _.-!!|||||
         .,uodWBBBBb.....||||       _.-!!|||||||||!:'
      !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
      !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
      !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
      !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
      !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
      `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
        `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
          `........::::::::::::::::;iof688888888888888888888b.     `
            `......:::::::::;iof688888888888888888888888888888b.
              `....:::;iof688888888888888888888888888888888899fT!
                `..::!8888888888888888888888888888888899fT|!^"'
                  `' !!988888888888888888888888899fT|!^"'
                      `!!8888888888888888899fT|!^"'
                        `!988888888899fT|!^"'
                          `!9899fT|!^"'
                            `!^"'



'''

for item in winapps.search_installed('chrome'):
    print(item)

time.sleep(69)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    platform = platform.system()

    print(platform)
    os.system('cls')

if platform == 'Windows':
  print(windows)
  print(f'OS Detected is {platform}')
  check = input('Is this correct? (y/n): ')
  if check == 'y':
    amount = 10
    print(f'Going to Install {amount} Applications')
    time.sleep(2)
    playsound('windows.mp3')
    print('')
    os.system("Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
    print('Installing FireFox...')
    os.system('choco install firefox -y --force')
    print('FireFox Installed!')
    print('Installing CCleaner...')
    os.system('choco install ccleaner -y --force')
    print('Ccleaner Installed...')
    print('Installing Git...')
    os.system('choco install git -y --force')
    print('Git Installed!')
    print('Installing Speccy...')
    os.system('choco install speccy -y --force')
    print('Speccy Installed!')
    print('Installing Scrcpy')
    os.system('choco install scrcpy -y --force')
    print('Scrcpy Installed!')
    print('Installing Discord...')
    os.system('choco install discord -y --force')
    print('Discord Installed!')
    print('Installing VLC...')
    os.system('choco install vlc -y --force')
    print('VLC Installed!')
    print('Installing Audacity...')
    os.system('choco install audacity -y --force')
    print('Audacity Installed!')
    print('Installing OBS...')
    os.system('choco install obs-studio -y --force')
    print('OBS Installed!')
    print('Installing Winrar...')
    os.system('choco install winrar -y --force')
    print('Installed Winrar!')

    time.sleep(5)


  elif check != 'y':
    playsound('Error.mp3')
    kb.press('alt+F4')
    
    
    


# elif platform == 'Linux':
    
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


