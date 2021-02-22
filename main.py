import time
from datetime import datetime
from pynput.keyboard import Controller, Key
import webbrowser

# 1 fetch zoom link from email (TODO)


# 2 automatically open and close the zoom

zoomlist = [
    #   INPUT   ZOOM URL                                                    		# start time     # End time
    ["https://vmware.zoom.us/j/94230697602?pwd=bXBJK2RMd2pvMStpYU0xdnFGZkJ6Zz09",      "9:00",     "16：00"]
]

def autoZoom(zoomlist):
    keyboard = Controller()
    isStarted = False
    for i in zoomlist:
        while True:
            if isStarted == False:
                if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                    print("open web browser")
                    webbrowser.open(i[0])
                    isStarted = True
            elif isStarted == True:
                if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                    print("close")
                    with keyboard.pressed(Key.cmd):
                        keyboard.press('w')
                        keyboard.release('w')
                    time.sleep(2)
                    keyboard.press(Key.enter)
                    isStarted = False
                    break

autoZoom(zoomlist)


