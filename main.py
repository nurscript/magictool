import base64
import pyautogui as ag
import time
import os
import sys
from datetime import datetime
from util import format_time, format_seconds
upload = "upload"
my_dir = os.path.join(os.getcwd(), upload)
f_list = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if os.path.isfile(os.path.join(my_dir,f))]

if len(f_list) == 0:
    print("NOTHING will happen no file")
    sys.exit(-1)
elif len(f_list) > 1:
    print(f_list[0])
    print("Only this file will be uploaded")

INPUT_FILE = f_list[0]
with open(INPUT_FILE, 'rb') as binary_file:
    binary_data = binary_file.read()
base64_encoded = base64.b64encode(binary_data).decode('utf-8')
total_symbols = len(base64_encoded)
print(f"symbols  {total_symbols}")
print(format_time(total_symbols))

print("You have 3 seconds to focus text editor.")
time.sleep(3)
start_time = datetime.now()

ag.write(base64_encoded, interval=0.0000001)
print("Finished in ", end=" ")
delta = datetime.now() - start_time
print(format_seconds(delta.seconds))

ag.press('esc')
ag.press(':')
ag.press('w')
ag.press('q')
ag.press('enter')
print("saved")

# os.system('shutdown /s /t 1')



