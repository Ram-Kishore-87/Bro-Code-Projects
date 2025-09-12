import pygame
import time
import datetime

def set_time(alarm_time ,sound_file):

    print(f"Alarm set for {alarm_time}")

    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time==alarm:
            print("Wake up!!!!")
            play_sound(sound_file)
            break
        time.sleep(1)

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ =="__main__":
        alarm=input("Enter your alarm time in HH:MM:SS format:")
        set_time(alarm,"dudududu_max_verstappe.mp3")
