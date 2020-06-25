import os
from auto import *
import keyboard as keyboard
from pyautogui import *
from pywinauto.application import Application
import subprocess
import pyperclip
import json,psutil


def Type(text=None, interval_seconds=0.001):
    '''
    Type text in the current active field. The first argument represent the text and is entered as a string. 
    The second variable is the time between two keystrokes. Pay attention that you can only press single 
    character keys. Keys like ":", "F1",... can not be part of the text argument.
    '''
    from pyautogui import typewrite
    # Set keyboard layout for Windows platform
    if platform.system() == 'Windows':
        from win32api import LoadKeyboardLayout
        LoadKeyboardLayout('00000409', 1)
    return typewrite(text, interval=interval_seconds)
def Wait(seconds=None):
    '''
    Stall the execution of the preceding functions for a specified number of seconds.
    '''
    sleep(seconds)

def Read_JSON():
    with open("config.json", encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return data
JSON = Read_JSON()

try:
	os.system("taskkill /f /im D2VN.EXE")
except:
	pass

#open tool
hotkey('ctrl','shift','l')


while True:
	try:
		Wait(1)
		app = Application().Connect(title=u'D2VN', class_name='WindowsForms10.Window.8.app.0.1fed012_r11_ad1')
		break
	except:
		pass
# class_name='WindowsForms10.Window.8.app.0.1fed012_r11_ad1'

Wait(1)
windowsformswindowappbarad = app.D2VN
windowsformsbuttonappbarad = windowsformswindowappbarad.Button11
windowsformsbuttonappbarad.ClickInput()




while True:
	try:
		Wait(1)
		app = Application().Connect(title=u'Diablo II', class_name='Diablo II')
		break
	except:
		pass

hotkey("enter")

while True:
	try:
		Wait(1)
		ClickOnImage('img\\1.png')
		break
	except:
		pass
Wait(2)
pyperclip.copy(str(JSON['pass']))
hotkey('ctrl','v')
hotkey("tab")
pyperclip.copy(str(JSON['id']))
hotkey('ctrl','v')
while True:
	try:
		Wait(1)
		ClickOnImage('img\\login.png')
		break
	except:
		pass

while True:
	try:
		Wait(1)
		ClickOnImage('img\\ok.png')
		break
	except:
		pass

intcout = 0
while True:
	try:
		Wait(1)
		ClickOnImage('img\\2.png')
		Type('room'+str(intcout))
		nameRoom = 'room'+str(intcout)
		hotkey("enter")
		intcout += 1
		try:
			Wait(1)
			ClickOnImage('img\\3.png')
		except:
			break
		
	except:
		pass

DisplayMessageBox("NAME ROOM: "+ nameRoom)
