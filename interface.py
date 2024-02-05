from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import calendar
import os.path
from sys import platform
import os
import sys
from configparser import ConfigParser
import time
from time import strftime
import subprocess

root = Tk()
root.title('Gamesim')
root.geometry('1870x1080')
root.attributes('-fullscreen', True)
config = ConfigParser()
config.read('main/savedata/savefile.ini')
directory = os.getcwd()


now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day


monthes = ['None', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augest', 'September', 'October', 'November', 'December']
iconx = int(config['DEFAULT']['iconx'])
apps = int(config['DEFAULT']['apps'])
allapps = config['DEFAULT']['allapps']
games = int(config['DEFAULT']['games'])
allgames = config['DEFAULT']['allgames']
coins = int(config['DEFAULT']['coins'])
time_now = f'{day}.{month}.{year}'
background_image = ['bg/wallpaper0.png', 'bg/wallpaper1.png']
image = int(config['DEFAULT']['image'])
toolbar_color = config['DEFAULT']['toolbar_color']
ids = []
password = config['DEFAULT']['password']

# Functions
def time():
	string = strftime('%H:%M:%S')
	timelabel.config(text = string)
	timelabel.after(1000, time)
# earning codes
def earn10():
	global coins, config
	config.set('DEFAULT', 'coins', str(coins+10))
	coins += 10

def earn20():
	global coins, config
	config.set('DEFAULT', 'coins', str(coins+20))
	coins += 20

def earn50():
	global coins, config
	config.set('DEFAULT', 'coins', str(coins+50))
	coins += 50

def earn100():
	global coins, config
	config.set('DEFAULT', 'coins', str(coins+100))
	coins += 100
# Returns
def returncoins():
	global coins
	return coins
def returnapps():
	global apps
	return apps
def returnallapps():
	global allapps
	return allapps
def returngames():
	global games
	return games
def returnallgames():
	global allgames
	return allgames

#updates
def update():
	os.execl(sys.executable, sys.executable, *sys.argv)
	
# main things
def startapp(appid):
	root.destroy()
	import appid
def quit():
	global config, root
	config.set('DEFAULT', 'entered_desktop_without_perms', 'True')
	MsgBox1 = messagebox.askquestion('Are you sure?', 'Are you sure you want to quit?', icon = 'warning')
	if MsgBox1 == 'yes':
		with open('main/savedata/savefile.ini', 'w') as configfile:
			config.write(configfile)
		sys.exit()




main = Frame(root)
xmain = -2
ymain = -2

# icons
shutdown_ico = PhotoImage(file='main/icons/shut_down.png')

cmd_ico = PhotoImage(file='main/icons/CMD.png')
settings_ico = PhotoImage(file='main/icons/settings.png')
browser_ico = PhotoImage(file='main/icons/browser.png')



backg = PhotoImage(file=f'main/{background_image[image]}')
background = Label(main, image=backg)
tool = Frame(background, bg=toolbar_color, width=1870, height=50)
date = Label(tool, text=time_now, fg='white', bg=toolbar_color, font='Arial 11')
timelabel = Label(tool, text='Time_Eror', fg='white', bg=toolbar_color, font='Arial 15')
shutdown = Button(tool, image=shutdown_ico, bg=toolbar_color, highlightthickness=0, relief=FLAT, command=quit)
border1 = Frame(tool, bg='grey', height=45, width=2)
yborder1 = 2

#game icons
def cmdopen():
	os.system(f'python {directory}\\main\\appdata\\CMD_app.py')

settings_open = False
def settingsopen():
	global settings_open
	settings_open = True
	os.system(f'python {directory}\\main\\appdata\\settings_app.py')
	if 'normal' == root.state():
		update()
def browseropen():
	os.system(f'python {directory}\\main\\appdata\\browser\\browser_app.py')

cmd_enter = Button(tool, image=cmd_ico, bg=toolbar_color, highlightthickness=0, relief=FLAT, command=cmdopen)
settings_enter = Button(tool, image=settings_ico, bg=toolbar_color, highlightthickness=0, relief=FLAT, command=settingsopen)
browser_enter = Button(tool, image=browser_ico, bg=toolbar_color, highlightthickness=0, relief=FLAT, command=browseropen)

#placement of buttons
settings_enter.place(x=68, y=5)
cmd_enter.place(x=108, y=5)
browser_enter.place(x=158, y=5)




# 
main.place(x=xmain, y=ymain)
tool.place(x=0, y=815)
background.pack(expand=True)
date.place(x=1440, y=25)
timelabel.place(x=1430, y=0)
border1.place(x=60, y=yborder1)
shutdown.place(x=12, y=5)

time()
if platform == "darwin":
    platform_error = messagebox.showwarning('You might expect some bugs.', 'Becouse your using a mac, there can be bugs.', icon='warning')


if config['DEFAULT']['entered_desktop_without_perms'] == 'True':
	MsgBox1 = messagebox.showwarning('You didnt enter the password', 'Enter the password', icon='warning')
	root.destroy()
root.mainloop()
