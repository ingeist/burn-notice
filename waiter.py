import serial
import numpy as np
from time import sleep,time
from crontab import CronTab

port = "/dev/ttyACM0"


ser = serial.Serial(port,2400,timeout = 0.050)
ser.baudrate=9600

#cron = CronTab(user='j')
#job = cron.new(command='python waiter.py')
#job.minute.on(0,15,23,30,45)

#cron.write()
sleepmin = 1 # number of minutes to wait/sleep

while (1==1):
   
   raw = ser.readline() # looks like b'0\r\n'
   string_n = raw.decode()
   string = string_n.rstrip()
   # if needed convert to float with flt = float(string) but check to make sure it's not nothing
   if (string != ''):
       integer = int(string)
       
       print(integer)
       
   #sleep(sleepmin*60)  # sleeps for number of minutes
   sleep(1)
