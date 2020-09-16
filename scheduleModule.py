import schedule
import time


def readingTime():
    print("YOU should be reading now...")

# time
schedule.every().day.at("23:02").do(readingTime)


while True:
    schedule.run_pending()

