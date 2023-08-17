import pyautogui as ag
import time

h=""
INPUT_FILE = "vash_text.txt"
with open(INPUT_FILE,'r') as code:
    h = code.read()

dumparray = str(h) 
## WAYTING THREE SECONDS TO GET PREPARED
## FOR AUTO TYPING FOCUSED TEXT EDITOR

## YOU CAN't STOP until it FINISHES
print("GET PREPARED")
time.sleep(3)
temp = str()

    
ag.typewrite(dumparray, interval=0.00001)


print("Finished")
