#wayset 3. Created by WebMast from WALM
#Wayset 4 update - lock buttons detect
#Wayset 5 Update - rewrite keyboard detect
#Wayset 5.5 - logs in /tmp and scroll button from keyboard detect

import os
import keyboard as kek
from time import sleep
from threading import Thread
import sys
import re

scroll_lock = []
enab_led_lib = {}
toggle_key = None

def script():

    def restart_script():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    try:
        os.remove('/tmp/leds.txt')
    except:
        pass

    for i in range(5):
        os.system('ls /sys/class/leds/ > /tmp/leds.txt')

        with open('/tmp/leds.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if 'input' in line]

        numbers = [item.split('::')[0][5:] for item in lines if 'scrolllock' in item]
        scroll_lock.clear()

        for number in numbers:
            scroll_lock.append(number)
            enab_led_lib[number] = 1
        os.remove('/tmp/leds.txt')

    def proc_detect():

        os.system('ls /sys/class/leds/ > /tmp/leds.txt')

        with open('/tmp/leds.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if 'input' in line]

        numbers = [item.split('::')[0][5:] for item in lines if 'scrolllock' in item]

        if numbers == scroll_lock:
            pass
        else:
            print('wayset restart')
            restart_script()

        scroll_lock.clear()
        for number in numbers:
            scroll_lock.append(number)

        os.remove('/tmp/leds.txt')

    def kbd_detect(e):
        e = e.replace('event', '')
        try:
            with open('/proc/bus/input/devices') as f:
                for sec in f.read().split('\n\n'):
                    if f'event{e}' in sec:
                        # Пробуем разные паттерны для input
                        patterns = [
                            r'/(input\d+)/',           # /.../input101/...
                            r'Sysfs=.*/(input\d+)',    # Sysfs=.../input101
                            r'input/input(\d+)'        # input/input101
                        ]
                        for pattern in patterns:
                            if m:=re.search(pattern, sec):
                                input_num = m[1] if len(m.groups()) > 0 else m[0]
                                if not input_num.startswith('input'):
                                    input_num = f"input{input_num}"
                                return input_num, f"event{e}"
        except:
            pass
        try:
            sysfs_path = f"/sys/class/input/event{e}/device"
            if os.path.islink(sysfs_path):
                real_path = os.path.realpath(sysfs_path)
                for part in real_path.split('/'):
                    if part.startswith('input'):
                        return part, f"event{e}"
        except:
            pass
        return None, f"event{e}"

    def toggle_led_pown():
        for i in scroll_lock:
            os.system(f" sh -c 'echo {enab_led_lib[i]} > /sys/class/leds/input{i}::scrolllock/brightness'")

    def on_key_press(event):
        global toggle_key, enable_led
        toggle_key = event.name
        keytarget = event.device[16:]

        if toggle_key == 'scroll lock':

            keytarget = kbd_detect(keytarget)[0][5:]

            if keytarget in enab_led_lib:
                if enab_led_lib[keytarget] == 1:
                    enab_led_lib[keytarget] = 0
                else:
                    enab_led_lib[keytarget] = 1
            else:
                enab_led_lib[keytarget] = 1

        if toggle_key == 'num lock':
            pass
        if toggle_key == 'caps lock':
            pass
        toggle_led_pown()

    kek.on_press(on_key_press)

    while True:
        proc_detect()
        toggle_led_pown()
        sleep(0.05)

print('Wayset. By WALM')
runscript = Thread(target=script).start()
