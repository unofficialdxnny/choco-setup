## Bored so wrote this script to automatically setup my pc for fresh windows installs

import os
import platform
from playsound import playsound
import keyboard as kb
import time 
import admin
import ctypes, sys

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
    time.sleep(2)
    playsound('windows.mp3')
    print('')
    print('Installing FireFox...')
    os.system('choco install firefox -y --force')
    print('FireFox Installed!')
    time.sleep(5)


  elif check != 'y':
    playsound('Error.mp3')
    kb.press('alt+F4')
    
    
    


# elif platform == 'Linux':
    
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


