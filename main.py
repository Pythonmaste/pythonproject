from tkinter import *
from turtle import *
import pyautogui
root = Tk()

## Made Eralp
color('red', 'yellow')
begin_fill()
def sep():
    forward(100)
def lef():
    left(90)
def rig():
    right(90)
def cic():
    circle(90)
def scr():
    screen = pyautogui.screenshot('screenshot.png')
    print(screen)




btn = Button(
    text="forward",
    command=sep
)
lef = Button(
    text="left",
    command=lef
)
ri = Button(
    text="right",
    command=rig
)
cic = Button(
    text="circle",
    command=cic
)
scre = Button(
    text="screen",
    command=scr
)

btn.pack()
lef.pack()
ri.pack()
cic.pack()
scre.pack()

root.mainloop()