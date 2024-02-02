import pyautogui as pg
import random
import time

#os.system("rundll32.exe powrprof.dll,SetSuspendState 0,0,0")  #Hibernate
#os.system("rundll32.exe user32.dll,LockWorkStation")    #Sleep


# An infinite while loop that will press the keys w/s/a/d for random intervals
# of time. This will keep the player moving in game so that they do not get
# kicked for being AFK.
def afk():
    while True:
        time_to_press = random.randint(1, 5)
        key_to_press = random.choice(['w', 's', 'a', 'd', 'w', 'w'])  #Triple weight to 'w' key
        message = f"Pressing {key_to_press} for {time_to_press} seconds"


        ### Uncomment this line if you wanna get heavily abused by your teammates
        # pg.press('enter')
        # pg.typewrite(message)
        # pg.press('enter')


        print(message)
        pg.keyDown(key_to_press)
        time.sleep(time_to_press)
        pg.keyUp(key_to_press)

        time.sleep(random.random())

if __name__ == "__main__":
    # Go to main display from side monitor
    time.sleep(1)
    pg.moveTo(200, 200)
    pg.click()
    time.sleep(1)

    try:
        afk()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
    



