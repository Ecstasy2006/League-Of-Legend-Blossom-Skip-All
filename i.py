import time
import pyautogui
from random import choices

#randomization of time it is in the 0.3xxx seconds range
def trial():
    return 2000 <= sorted(choices(range(6000), k=5))[2] < 4000

coolTiming = sum(trial() for i in range(6000)) / 10000

#Click on the damn shit
pyautogui.click(pyautogui.locateCenterOnScreen('exclamation.png'))
time.sleep(coolTiming)
pyautogui.click(pyautogui.locateCenterOnScreen('skipAll.png'))
time.sleep(coolTiming)
pyautogui.click(pyautogui.locateCenterOnScreen('skip.png'))
time.sleep(coolTiming*3)
pyautogui.press('esc')
