import time
import datetime


time_in_minutes= 45 
#print(time.time())
timerr=0
while timerr <= time_in_minutes:
    print(time.ctime(),end='\r')
    time.sleep(1)
    timerr += 1

if __name__=='__main__':
    main()
