import os
import time
import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day

while True:
    if year==datetime.datetime.now().year and month==datetime.datetime.now().month and day==datetime.datetime.now().day:
        pass
    elif datetime.datetime.now().hour>1:
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        for i in range(1,3):
            print(i)
            str1 = 'scrapy crawl uploadheath -a twice='+str(i)
            os.system(str1)
            time.sleep(10)





