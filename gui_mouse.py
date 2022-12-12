from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('โปรแกรมสั่งกดปฏิทิน')
GUI.geometry('500x300')

def calander():
    pg.click(1880,1056)

def start():
    pg.click(728,1059)

def Google():
    webbrowser.open('https://www.google.com')

B1 = ttk.Button(GUI,text='Calander1',command=calander)
B1.pack(ipadx=20,ipady=20,pady=5)

B2 = ttk.Button(GUI,text='Start',command=start)
B2.pack(ipadx=20,ipady=20,pady=20)

B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20,ipady=20)



GUI.mainloop()