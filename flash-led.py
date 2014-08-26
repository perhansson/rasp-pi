import RPi.GPIO as GPIO
import time
import string

GPIO.setmode(GPIO.BCM)

led_green = 18
led_red = 22

GPIO.setup(led_green,GPIO.OUT)
GPIO.setup(led_red,GPIO.OUT)

while(True):
    print("Tell me how many times to blink:")
    s = input("How many times to blink the green LED? ")
    print(s)
    n_green_blink = int(s)
    s = input("How many times to blink the red LED? ")
    print("Ok, " + s + " times")
    n_red_blink = int(s)
    i = 0
    n_max = max(n_green_blink,n_red_blink)
    print ("Watch the LEDs")
    while(i<n_max):
        if i<n_red_blink:
            GPIO.output(led_red,1)
        if i<n_green_blink:
            GPIO.output(led_green,1)
        time.sleep(1)
        if i<n_red_blink:
            GPIO.output(led_red,0)
        if i<n_green_blink:
            GPIO.output(led_green,0)        
        time.sleep(1)
        i=i+1
    print("Done blinking ")


GPIO.cleanup()
