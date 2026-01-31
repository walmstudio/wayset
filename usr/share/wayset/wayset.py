#wayset 3. Created by WebMast from WALM
#Wayset 4 update - lock buttons detect
#Wayset 5 Update - rewrite keyboard detect

import os
import keyboard as kek
from time import sleep
from threading import Thread
import sys

scroll_lock = []
enable_led = 1
toggle_key = None

def script():
    def restart_script():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    try:
        os.remove('leds.txt')
    except:
        pass

    for i in range(5):
        os.system('ls /sys/class/leds/ > leds.txt')

        with open('leds.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if 'input' in line]

        numbers = [item.split('::')[0][5:] for item in lines if 'scrolllock' in item]
        scroll_lock.clear()

        for number in numbers:
            scroll_lock.append(number)
        os.remove('leds.txt')

    def proc_detect():

        os.system('ls /sys/class/leds/ > leds.txt')

        with open('leds.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if 'input' in line]

        numbers = [item.split('::')[0][5:] for item in lines if 'scrolllock' in item]

        if numbers == scroll_lock:
            pass
        else:
            restart_script()

        scroll_lock.clear()
        for number in numbers:
            scroll_lock.append(number)

        os.remove('leds.txt')

    def toggle_led_pown():
        for i in scroll_lock:
            os.system(f" sh -c 'echo {enable_led} > /sys/class/leds/input{i}::scrolllock/brightness'")

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

    kek.on_press(on_key_press)

    while True:
        if enable_led == 1:
            proc_detect()
            toggle_led_pown()
            sleep(0.05)
        else:
            continue

print('Wayset. By WALM')
runscript = Thread(target=script).start()