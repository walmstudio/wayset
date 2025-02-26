#wayset 3. Created by WebMast from WALM

#Wayset 4 update - lock buttons detect

import os
import keyboards
import keyboard as kek
from time import sleep

scroll_lock = []
enable_led = 1
toggle_key = None

try:
    scroll_lock.clear()
except:
    pass

append_index = keyboards.minimum_led

for i in range(5):
    for i in range(append_index):
        detect = os.system(f" sh -c 'echo {enable_led} > /sys/class/leds/input{i}::scrolllock/brightness'")
        if detect == 0:
            if i in scroll_lock:
                pass
            else:
                scroll_lock.append(i)
        else:
            continue
    if len(scroll_lock) >= keyboards.indexes:
        break
    else:
        if append_index == keyboards.maximum_led:
            pass
        else:
            append_index += 100
            
def scroll_detect_index():
    global scroll_lock, append_index

    append_index = keyboards.maximum_led

    try:
        scroll_lock.clear()
    except:
        pass

    for i in range(5):
        for i in range(append_index):
            detect = os.system(f" sh -c 'echo {enable_led} > /sys/class/leds/input{i}::scrolllock/brightness'")
            if detect == 0:
                if i in scroll_lock:
                    pass
                else:
                    scroll_lock.append(i)
            else:
                continue
        if len(scroll_lock) == keyboards.indexes:
            break
        else:
            if append_index == keyboards.maximum_led:
                pass
            else:
                append_index += 100

def toggle_led_pown():
    detect_scroll = os.system(f" sh -c 'echo {enable_led} > /sys/class/leds/input{i}::scrolllock/brightness'")

    if detect_scroll == 0:
        print(f'{i} = {detect_scroll}')

        if len(scroll_lock) == keyboards.indexes:
            pass
        else:
            scroll_detect_index()
    else:
        scroll_lock.remove(i)
        print(scroll_lock)

def on_key_press(event):
    global toggle_key, enable_led
    toggle_key = event.name

    if toggle_key == 'scroll lock':
        if enable_led == 0:
            enable_led = 1
            toggle_led_pown()
            sleep(0.05)
        elif enable_led == 1:
            enable_led = 0
            toggle_led_pown()
            sleep(0.05)
    if toggle_key == 'num lock':
        if enable_led == 0:
            enable_led = 0
            sleep(0.05)
        else:
            enable_led = 1
            sleep(0.05)
    if toggle_key == 'caps lock':
        if enable_led == 0:
            enable_led = 0
            sleep(0.05)
        else:
            enable_led = 1
            sleep(0.05)

kek.on_press(on_key_press)

while True:
    for i in scroll_lock:

        if enable_led == 1:
            detect_scroll = os.system(f" sh -c 'echo {enable_led} > /sys/class/leds/input{i}::scrolllock/brightness'")

            if detect_scroll == 0:
                print(f'{i} = {detect_scroll}')

                if len(scroll_lock) == keyboards.indexes:
                    pass
                else:
                    scroll_detect_index()
            else:
                scroll_lock.remove(i)
                print(scroll_lock)
        elif enable_led == 0:
            pass
