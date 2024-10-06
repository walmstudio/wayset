#wayset 2. Created by WebMast from WALM

import os

scroll_lock = []


try:
    scroll_lock.clear()
except:
    pass

for i in range(100):
        detect = os.system(f" sh -c 'echo 1 > /sys/class/leds/input{i}::scrolllock/brightness'")
        if detect == 0:
            scroll_lock.append(i)
        else:
            continue

while True:
    for i in scroll_lock:
        detect_scroll = os.system(f" sh -c 'echo 1 > /sys/class/leds/input{i}::scrolllock/brightness'")

        if detect_scroll == 0:
            pass
        else:
            import scrolldetect
