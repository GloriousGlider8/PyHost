import keyboard as k
import os
import time

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
LINE_UC = LINE_UP + LINE_CLEAR

def upAndClear():
    print(LINE_UP, end=LINE_CLEAR)

def selPrompt(options, icons, intro):
    os.system("cls")
    print(intro)
    print("\nUse [UP] and [DOWN] to move cursor.\nUse [RIGHT] to select.\n")

    print("[" + icons[0] + "] " + options[0])

    for i in range(len(options) - 1):
        print("[ ] " + options[i + 1])

    temp = 0
    temp1 = 0

    while True:
        time.sleep(0.15)

        if temp1 != temp:
            for _ in range(len(options)):
                upAndClear()
            for i in range(len(options)):
                if temp == i:
                    print("[" + icons[i] + "] " + options[i])
                else:
                    print("[ ] " + options[i])
                
            temp1 = temp

        if k.is_pressed("up"):
            if temp > 0:
                temp = temp - 1
                                    
        elif k.is_pressed("down"):
            if temp < len(options) - 1:
                temp = temp + 1

        elif k.is_pressed("right"):
            os.system("cls")
            return temp
