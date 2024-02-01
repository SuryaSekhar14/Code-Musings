import pyautogui as pg
import time
import os

time.sleep(1)

# Go to main display from side monitor
pg.moveTo(200, 200)
pg.click()
time.sleep(1)


while True:
    # s = pg.locateOnScreen("bot.jpeg", confidence=0.9)

    # try:
    #     print(pg.locateOnScreen('bot-full.jpeg', grayscale=True))
    #     # loc = pg.locateOnScreen('bot-full.jpeg', grayscale=True, confidence=0.9)
    #     # print('image found')
    #     # pg.moveTo(loc)
    #     # pg.click()
    # except pg.ImageNotFoundException:
    #     print('ImageNotFoundException: image not found')
    # except Exception as e:
    #     print(e)
    #     print('Exception: image not found')


    try:
        loc = pg.locateOnScreen('cardboard.png', grayscale=True, confidence=0.9)
        print("image found at: " + str(loc))
        pg.moveTo(loc)
        pg.click()
    except pg.ImageNotFoundException:
        print("ImageNotFoundException: Image Not Found")
    except Exception as e:
        print(f"Exception occoured: {e}")



