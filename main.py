from tkinter import *
from tkinter import ttk
import time
import ctypes

mouse = ctypes.windll.user
state = False

def StateIsF():
    global state
    global counter
    if state == True:
        x = 0
        state = False

def StateIsT():
    global state
    global x
    if state == False:
        x = 0
        state = True

    else:
        state = True

root = Tk()
root.title("AutoClocker")

amount = StringVar()
speed = StringVar()

amount.set(0)
speed.set(100)
mainframe = ttk.Frame(root)
mainframe.grid(padx=5, pady=5)

amlable = ttk.Label(mainframe, text = "Количество кликов \n (оставьте 0 для значения по улмолчанию)").grid(column=1, row =1, sticky=W)
speedlable = ttk.label(mainframe, text = "Интервал между кликами \n (в миллисекундах)").grid(column=1, row=2, sticky=W)
amountEntry = ttk.Entry(mainframe, textvariable=amount, width=5).grid(column=2, row=1)