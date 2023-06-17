import pyautogui
import time

message = "HAIIII"

n = 1000

time.sleep(6)


for i in range(n) :
    pyautogui.typewrite(message + '\n')