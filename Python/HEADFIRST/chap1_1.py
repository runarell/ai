from datetime import datetime
from turtle import right
import random
import time

odds = []
for i in range(60):
    if i % 2 != 0:
        odds.append(i)
# print(odds)

for i in range(5):
    right_this_minute = datetime.today().second

    if right_this_minute in odds:
        print("this second seems a little odd")
    else:
        print("Not an odd second")
    wait_time = random.randint(1, 5)
    time.sleep(wait_time)
