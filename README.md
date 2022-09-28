# IBM-Project-13414-1659518228
Smart Solutions For Railways
import numpy as np
from numpy import random
from playsound import playsound
import time
sound='Alarm.mp3'
temp=random.randint(1,200)
moi=random.randint(1,100)
print(temp,moi)
if(temp>=100 and moi<=50):
    playsound(sound)
