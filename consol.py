import pyautogui
import time
import os
import sys
import datetime


# This is a simple script that takes screenshots
# form your system and will save them in its pics folder.
# The script is just like "win+sysrq" in windows.


DATE_FORMAT = "%b_%d_%Y-%H_%M"
MAIN_DIR = "./pics/"
FORMAT = ".png"


def folder():
	if not os.path.exists(MAIN_DIR):
		os.mkdir(MAIN_DIR)


def path():
	date = datetime.datetime.now()	
	string = date.strftime(DATE_FORMAT)	
	return MAIN_DIR + string + FORMAT


def screenshot():
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(path())


def wait(limit=2):
	time.sleep(limit)


def execute():
	print("> System got executed ...")
	folder()
	wait()
	screenshot()
	print("< Screen token.")


if __name__ == "__main__":
	execute()	