
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ctypes
import sys
from configparser import ConfigParser


root = Tk()
root.title('CMD')
root.geometry('500x400')
root.attributes("-fullscreen", True)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
config = ConfigParser()
config.read('main/savedata/savefile.ini')

password = config['DEFAULT']['password']
dir = config['DEFAULT']['dir']

def quit_app():
	global config
	config.set('DEFAULT', 'password', f'{password_entry.get()}')
	config.set('DEFAULT', 'entered_desktop_without_perms', 'True')
	with open('main/savedata/savefile.ini', 'w') as configfile:
		config.write(configfile)
	root.destroy()

quitsettings = Button(width=3, height=1, text='X', bg='Red', command=quit_app)



general = LabelFrame(text='General', height=200, width=1450)
password_label = Label(general, text='Password', font='Arial 15')
password_entry = Entry(general, width=20, show='*')
password_entry.insert(0, password)

quitsettings.place(x=1506, y=0)
general.place(x=30, y=30)
password_label.place(x=10, y=10)
password_entry.place(x=115, y=16)



if config['DEFAULT']['entered_desktop_without_perms'] == 'True':
	MsgBox1 = messagebox.showwarning(
		'You didnt enter the password', 'Enter the password', icon='warning')
	root.destroy()
root.mainloop()
