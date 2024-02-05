from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from configparser import ConfigParser
import sys
import time
import os
import subprocess


root = Tk()
root.title('Gamesim')
root.geometry('1870x1080')
root.attributes('-fullscreen', True)
root.lift()
config = ConfigParser()
config.read('main/savedata/savefile.ini')
config.set('DEFAULT', 'dir', f'{os.getcwd()}')


password = config['DEFAULT']['password']

def launchdesk(event):
	global passwordentry, password, config, userpic, hint, loadingbar
	config.set('DEFAULT', 'entered_desktop_without_perms', 'False')
	with open('main/savedata/savefile.ini', 'w') as configfile:
		config.write(configfile)
	entryout = passwordentry.get()
	if str(entryout) == str(password):
		loadingbar.place(x=618, y=478)
		for progress in range(100):
			loadingbar['value'] += 1
			root.update_idletasks()
			time.sleep(0.03)
			if loadingbar['value'] >= 99:
				root.destroy()
				import interface
	else:
		hint.config(text='                       Password is wrong.')
		root.after(2000, lambda :hint.config(text=''))

userpicpi = PhotoImage(file='user_icons/userpic.png')



main = Frame(height=864, width=1536, bg='Blue')
userpic = Label(main, image=userpicpi, bg='Blue')
passwordentry = Entry(main, width=25, show='*')
hint = Label(main, text='', bg='Blue', fg='Red')
loadingbar = ttk.Progressbar(main, orient=HORIZONTAL, length=300, mode='determinate')


main.place(x=0, y=0)
userpic.place(x=650, y=250)
passwordentry.place(x=688, y=478)
hint.place(x=628, y=500)

if config['DEFAULT']['passlabelshow'] == 'False':
	config.set('DEFAULT', 'passlabelshow', 'True')
	hint.config(text='The password is: poo, you can change it after.')
	with open('main/savedata/savefile.ini', 'w') as configfile:
		config.write(configfile)
passwordentry.bind('<Return>', launchdesk)

time.sleep(1)
root.lift()
root.mainloop()
