# Alarm Clock Application

import time
import datetime 
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"


import pygame

def set_alarm(alarm_time):
    print("Alarm set for:", alarm_time)
    while True:
        current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
        current_time = datetime.datetime.strptime(current_time, "%H:%M:%S").time()
        print("Current time:", current_time)
        time.sleep(1)  
        if current_time >= alarm_time:
            print("Alarm ringing! Wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load("alarm_sound.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break

def main():
    set_alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    try:
        alarm_time = datetime.datetime.strptime(set_alarm_time, "%H:%M:%S").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return
    print("Setting alarm...")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()