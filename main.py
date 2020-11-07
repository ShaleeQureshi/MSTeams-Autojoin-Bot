import subprocess
import pyautogui
import time

subprocess.Popen(
    'C:\\Users\\shale\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"')

join = None
while join is None:
    join = pyautogui.locateCenterOnScreen("teamsp2.PNG", grayscale=True)
pyautogui.moveTo(join)
pyautogui.click()
print("opened TEAM")

time.sleep(1)

teamsp2 = pyautogui.locateCenterOnScreen("teamsp3.PNG", grayscale=True)
pyautogui.moveTo(teamsp2)
pyautogui.click()
print("opened TEAMV2")

time.sleep(1)

deca = pyautogui.locateCenterOnScreen("deca.PNG", grayscale=True)
pyautogui.moveTo(deca)
pyautogui.click()
print("opened deca")

time.sleep(1)

finance = pyautogui.locateCenterOnScreen("finance.PNG", grayscale=True)
pyautogui.moveTo(finance)
pyautogui.click()
print("opened finance")

time.sleep(1)

join = pyautogui.locateCenterOnScreen("join.PNG", grayscale=True)
pyautogui.moveTo(join)
pyautogui.click()
print("joined")
