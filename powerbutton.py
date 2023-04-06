from gpiozero import Button
# from signal import pause
import os
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__),'../dev_web'))
sys.path.append('../dev_web')
from app_threading import write_oled
import time

button = Button(4, hold_time=3)

pressed = 0

def button_pressed():
    try:
        global pressed
        print(f"Button was pressed setting Oled to: {pressed}")
        if pressed == 0:
            write_oled('IP')
            pressed += 1
        elif pressed == 1:
            write_oled('CPU')
            pressed += 1
        elif pressed == 2:
            write_oled('Mem')
            pressed += 1
        else:
            write_oled('Disk')
            pressed = 0
    except Exception as e:
        print(e)

def button_held():
    print("Button was held")
    print("Shutting Down")
    os.system("sudo shutdown -h now")

def button_released():
    print("Button was released")
    time.sleep(1)

def init():
    button.when_pressed = button_pressed
    button.when_held = button_held
    button.when_released = button_released

# pause()

# if __name__ == '__main__':
#     button_pressed()