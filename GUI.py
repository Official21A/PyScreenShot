import pyautogui
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()


def takeScreenshot ():
    global root
    root.iconify()

    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

    root.deiconify()


def init():

	canvas1 = tk.Canvas(root, width = 300, height = 300)
	canvas1.pack()

	myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
	canvas1.create_window(150, 150, window=myButton)

	root.mainloop()


if __name__ == "__main__":
	init()	