import os
import globalvars
import json

pressed = 1

def read_oled(command):
    print(command)

def button_pressed():
    try:

        absolute_path = os.path.dirname(__file__)
        print(absolute_path)
        relative_path = "state.json"
        full_path = os.path.join(absolute_path, relative_path)
        print(full_path)
        # Opening JSON file
        with open(full_path, 'r') as openfile: # reletive path todo
            # Reading from json file
            json_object = json.load(openfile)
            print(json_object)
        global pressed
        print(f"Button was pressed setting Oled to: {pressed}")
        if pressed == 0:
            read_oled('IP')
            pressed += 1
            globalvars.changed = True
        elif pressed == 1:
            read_oled('CPU')
            pressed += 1
            globalvars.changed = True
            thismightwork = json_object["system"]["CPU"]
            print(thismightwork)
        elif pressed == 2:
            read_oled('Mem')
            pressed += 1
            globalvars.changed = True
        else:
            read_oled('Disk')
            pressed = 0
            globalvars.changed = True
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # print('Enter 1-4')
    # pressed = input()
    # pressed = int(pressed)
    pressed = 1
    button_pressed()
    print(globalvars.changed)
