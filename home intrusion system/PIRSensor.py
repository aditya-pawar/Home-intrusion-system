import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)

GPIO.setup(26,GPIO.IN)
try:
    while True:
        if(GPIO.input(26)==1):
	         
            	 print(" detected")
		 subprocess.call(["python","capture.py"])
		 subprocess.call(["python","mail.py"])
		 subprocess.call(["python","sms.py"])
                 time.sleep(10)
        else:
            
            print("Not Detected")
            time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()