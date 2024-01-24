from tkinter import *
from tkinter import ttk
import time
import ctypes

mouse = ctypes.windll.user32
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
speedlable = ttk.Label(mainframe, text = "Интервал между кликами \n (в миллисекундах)").grid(column=1, row=2, sticky=W)
amountEntry = ttk.Entry(mainframe, textvariable=amount, width=5).grid(column=2, row=1)
speedEntry = ttk.Entry(mainframe, textvariable=speed, width=5).grid(column=2, row=2)
startButton = ttk.Button(mainframe, text="Начать", width=10, command=StateIsT).grid(column=1, row=3, columnspan=2, sticky=W)
stopButton = ttk.Button(mainframe, text="Стоп", width=10,command=StateIsF).grid(column=2, row=3, columnspan=2,sticky=E)

mainframe.bind("<F1>", StateIsT())
mainframe.bind("<F3>", StateIsF())

time_counter=0
x=0

while True:
    time_counter+=1
    if state==True:
        amount = int(amount.get())
        speed = int(speed.get())
        print(state)
        if amount==0:
            time.sleep(speed/1000)
            mouse.mouse_event(2,0,0,0,0)
            mouse.mouse_event(4,0,0,0,0)
            x+=1
            print("Кликнуто " +x + " раз")

        elif x <amount and state == True:
            time.sleep(speed / 1000)
            mouse.mouse_event(2, 0, 0, 0, 0)
            mouse.mouse_event(4, 0, 0, 0, 0)
            x += 1
            print("Кликнуто " + x + " раз")
            if x == amount:
                state = False

    root.update()