import pyautogui as pg

pg.moveTo(800,980)
pg.click()

for i in range(1000):
    pg.write('pls hunt')
    pg.press('enter')
    pg.write('pls fish')
    pg.press('enter')
    pg.write('pls dig')
    pg.press('enter')
    pg.write('pls crime')
    pg.press('enter')
    pg.write('pls search')
    pg.press('enter')
    pg.sleep(40)

