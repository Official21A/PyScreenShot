import pyautogui
import tkinter as tk
from tkinter import filedialog

# An user interface program of taking screenshots,
# init we close the gui window and take screenshots and
# then we let you choose the path to save the file.

root = tk.Tk()


def takeScreenshot ():
	# screen shot tacker function
    global root
    root.iconify()

    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

    root.deiconify()


def init():
	# to start the program
	root.title("Shotter")
	root.resizable(width=False, height=False)

	canvas1 = tk.Canvas(root, width = 300, height = 150, border=0)
	canvas1.configure(bg='#33001a')
	canvas1.pack()

	myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, 
						 bg='#ff8533',fg='white',font= 12)
	canvas1.create_window(150, 75, window=myButton)

	root.mainloop()


if __name__ == "__main__":
	init()	