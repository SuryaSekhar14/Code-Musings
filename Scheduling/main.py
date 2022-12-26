import schedule
import time as tm
from datetime import time, timedelta, datetime

def job():
    print("I'm working...")

schedule.every().second.do(job)

while True:
    schedule.run_pending()
    tm.sleep(10)