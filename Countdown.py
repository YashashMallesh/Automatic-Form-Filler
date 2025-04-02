#! Python3
# Countdown.py - A countdown script

import time,subprocess
# Countdown from 60
timeLeft = 60
while timeLeft > 0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
# At the end of the countdown, play a sound file.
subprocess.Popen(['start','alarm.wav'],shell=True)