import time
import playsound
import winsound

from datetime import datetime

Time = int(input("enter the time in sec :"))

current_time = datetime.now()

for x in reversed(range(0 , Time)) :

    sec = x % 60

    min = int((x / 60)) % 60

    hour = int((x / 3600))

    print(f"{hour:02}:{min:02}:{sec:02}")

    time.sleep(1)
 
for y in range(1 , 16):
    frequency = 2500
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 2500
    duration = 500
    winsound.Beep(frequency, duration)
   

    
    
    
    
    