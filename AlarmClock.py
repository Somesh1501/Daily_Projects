import os
import argparse
from selenium.webdriver import Chrome
import time , datetime

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('time_to_wakeup' , help = "Enter time to wake up.\t")
    parser.add_argument('link', help = "Enter Url of video to play at wake up.\n")
    args = parser.parse_args()
    time_to_alarm = args.time_to_wakeup
    link = args.link
except:
    time_to_alarm = input("Enter time to wake up in form %H:%M:%S")
    link = input("Enter link of youtube video to play at time to wakeup.")
while True:
    tim = datetime.datetime.now()
    current_time = "%02d:%02d:%02d"%(tim.hour,tim.minute,tim.second)
    if current_time == time_to_alarm:
        browser = Chrome()
        browser.get(link)
        break
    print(current_time,flush=True,end = "\r")
    time.sleep(1)
