import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from time import sleep  # pull in the sleep function from time module  
  

# ingore any warnings
GPIO.setwarnings(False)


GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

#GPIO.setup(GPIO_STOP1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
#blue17 = GPIO.PWM(17, 100)    # create object blue17 for PWM on port 25 at 100 Hertz  
#blue18 = GPIO.PWM(18, 100)      # create object blue18 for PWM on port 24 at 100 Hertz  
  
#blue17.start(0)              # start blue17 led on 0 percent duty cycle (off)  
#blue18.start(100)              # blue18 fully on (100%)  
  
# now the fun starts, we'll vary the duty cycle to   
# dim/brighten the leds, so one is bright while the other is dim  
  
pause_time = 0.02           # you can change this to slow down/speed up  
  
             # stop the blue18 PWM output  
GPIO.cleanup() 
