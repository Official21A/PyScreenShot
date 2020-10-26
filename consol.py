import pyautogui
import time


def screenshot():
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(r'new_img.png')


def wait(limit):
	time.sleep(limit)


def execute():
	print("> System got executed ...")
	wait(2)
	screenshot()
	print("< Screen token.")


if __name__ == "__main__":
	execute()	