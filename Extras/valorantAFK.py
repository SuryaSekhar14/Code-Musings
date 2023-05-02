import pyautogui as pg
import time
import os

#os.system("rundll32.exe powrprof.dll,SetSuspendState 0,0,0")  #Hibernate

#os.system("rundll32.exe user32.dll,LockWorkStation")    #Sleep

time.sleep(5)
print(pg.position())


pg.click(344, 377)


while 1:
    for i in range(100000):
        pg.keyDown('w')
        pg.keyUp('w')

    for i in range(1000):
        pg.keyDown('a')
        pg.keyUp('a')

    for i in range(1000):
        pg.keyDown('s')
        pg.keyUp('s')

    for i in range(1000):
        pg.keyDown('d')
        pg.keyUp('d')




