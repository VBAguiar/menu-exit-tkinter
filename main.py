from tkinter import *
from os import system


screen = Tk() # Screen

def shutdown():
	system('sudo shutdown')

def reboot():
	system('sudo reboot')

screen.title('Menu Exit') # Title
screen.geometry('160x130') # Screen Size

shutdownB = Button(screen, text = 'Shutdown', command = shutdown, width = 10, height = 2) # Shutdown Button
rebootB = Button(screen, text = 'Reboot', command = reboot, width = 10, height = 2) # Reboot Button

shutdownB.pack()
rebootB.pack()
screen.mainloop() # End Screen
