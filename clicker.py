import time
import random
import sys

from pyautogui import click
from tkinter import *
from tkinter.messagebox import showinfo
from multiprocessing import Process

def Help():
    showinfo(title='Help', message="Default value for minimum is: 1 second. For maximum it's: 5 seconds")

def intestines():
    try:
        min = float(entry1.get())
    except ValueError:
        min = 1
    try:
        max = float(entry2.get())
    except ValueError:
        max = 6

    time.sleep(1)

    if min > max:
        showinfo(title="Error", message="Maximum value is smaller than minimum value.")
        return
    else:
        pass

    while True:
        time.sleep(random.uniform(min, max))
        click()

def clicki():
    global x
    x = Process(target=intestines)
    x.start()

def unenter():
    global x
    x.terminate()
    sys.exit(0)


win = Tk()
win.title("Autoclicker")

button_click = Button(win,
                      text='Start',
                      command=clicki)
button_help = Button(win,
                     text='Help',
                     command=Help)
button_quit = Button(win,
                     text='Quit',
                     command=unenter)
entry1 = Entry(win,
               textvariable=min,
               width=5)
entry2 = Entry(win,
               textvariable=max,
               width=5)
label1 = Label(win,
               text='Minimum')
label2 = Label(win,
               text='Maksimum')

def clickerino():
    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)
    entry1.grid(row=1, column=0)
    entry2.grid(row=1, column=1)
    button_quit.grid(row=3, column=1)
    button_help.grid(row=2, column=1)
    button_click.grid(row=2, column=0)

    win.mainloop()

if __name__ == '__main__':
    begin = Process(group=None, target=clickerino, name=None, args=(), kwargs={})
    begin.start()
