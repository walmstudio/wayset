#wayset 3. Created by WebMast from WALM

#Wayset 4 update - lock buttons detect

import os
import keyboards
import keyboard as kek
from time import sleep
from importlib import reload
from threading import Thread
import sys

scroll_lock = []
enable_led = 1
toggle_key = None

def script():
    try:
        scroll_lock.clear()
    except:
        pass

    append_index = keyboards.minimum_led

    for i in range(5):
        for i in range(append_index):
            detect = os.system(f" sh -c 'echo 1 > /sys/class/leds/input{i}::scrolllock/brightness'")
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

    def toggle_led_pown():
        for i in scroll_lock:
            detect_scroll = os.system(f" sh -c 'echo {enable_led} > /sys/class/leds/input{i}::scrolllock/brightness'")

    def on_key_press(event):
        global toggle_key, enable_led
        toggle_key = event.name

        if toggle_key == 'scroll lock':
            if enable_led == 0:
                enable_led = 1
            elif enable_led == 1:
                enable_led = 0
        if toggle_key == 'num lock':
            pass
        if toggle_key == 'caps lock':
            pass
        toggle_led_pown()
        
    

    def restart_script():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    kek.on_press(on_key_press)

    while True:
        if enable_led == 1:
            for i in scroll_lock:
                detect_scroll = os.system(f" sh -c 'echo {enable_led} > /sys/class/leds/input{i}::scrolllock/brightness'")

                if detect_scroll == 0:
                    if len(scroll_lock) == keyboards.indexes:
                        pass
                    else:
                        restart_script()
                else:
                    scroll_lock.remove(i)
        else:
            continue

runscript = Thread(target=script).start()
