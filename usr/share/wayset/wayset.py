#wayset 3. Created by WebMast from WALM

import os
import keyboards

scroll_lock = []

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
            
def scroll_detect_index():
    global scroll_lock, append_index

    append_index = keyboards.maximum_led

    try:
        scroll_lock.clear()
    except:
        pass

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
        if len(scroll_lock) == keyboards.indexes:
            break
        else:
            if append_index == keyboards.maximum_led:
                pass
            else:
                append_index += 100

while True:
    for i in scroll_lock:
        detect_scroll = os.system(f" sh -c 'echo 1 > /sys/class/leds/input{i}::scrolllock/brightness'")

        if detect_scroll == 0:
            print(f'{i} = {detect_scroll}')

            if len(scroll_lock) == keyboards.indexes:
                pass
            else:
                scroll_detect_index()
        else:
            scroll_lock.remove(i)
            print(scroll_lock)
