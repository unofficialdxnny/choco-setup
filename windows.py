## Bored so wrote this script to automatically setup my pc for fresh windows installs

## Bored so wrote this script to automatically setup my pc for fresh windows installs

import os
import platform
from playsound import playsound
import keyboard as kb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests

import time 

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
platform = platform.system()

print(platform)
os.system('cls')

if platform == 'Windows':
    print(f'{windows}')
    playsound('windows.mp3')
    print('')
    requests.get('https://code.visualstudio.com/docs/?dv=win')
    





elif platform == 'Linux':
    print('False')
