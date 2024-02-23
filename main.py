from datetime import datetime
import os
print(os.getcwd())
now = datetime.now()
def fun(event):
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))