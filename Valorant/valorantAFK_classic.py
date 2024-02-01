import pyautogui as pg
import time
import os
import random

#os.system("rundll32.exe powrprof.dll,SetSuspendState 0,0,0")  #Hibernate
#os.system("rundll32.exe user32.dll,LockWorkStation")    #Sleep


# Go to main display from side monitor
time.sleep(1)
pg.moveTo(200, 200)
pg.click()


# An infinite while loop that will press the keys w/s/a/d for random intervals
# of time. This will keep the player moving in game so that they do not get
# kicked for being AFK.
while True:
    time_to_press = random.randint(1, 10)

    key_to_press = random.choice(['w', 's', 'a', 'd'])

    pg.keyDown(key_to_press)
    time.sleep(time_to_press)
    pg.keyUp(key_to_press)

    time.sleep(1)





